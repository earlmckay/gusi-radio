#!/usr/bin/env python3

import subprocess
import time
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from urllib.parse import parse_qs
import threading

class WifiSetupHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Captive Portal Detection Support
        captive_portal_paths = [
            '/generate_204',  # Android
            '/connecttest.txt',  # Windows
            '/ncsi.txt',  # Windows
            '/hotspot-detect.html',  # iOS
            '/library/test/success.html',  # iOS
            '/success.txt'  # OS X
        ]
        
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('/home/gusi/gusi-radio/wifi-setup/wifi_fallback.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path in captive_portal_paths:
            # Redirect captive portal detection attempts to our setup page
            self.send_response(302)
            self.send_header('Location', 'http://192.168.4.1/')
            self.end_headers()
        elif self.path == '/scan':
            networks = self.scan_networks()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(networks).encode())
        elif self.path.startswith('/source/'):
            # Serve static resources like images or CSS
            try:
                resource_path = '/home/gusi/gusi-radio' + self.path
                with open(resource_path, 'rb') as file:
                    self.send_response(200)
                    if self.path.endswith('.svg'):
                        self.send_header('Content-type', 'image/svg+xml')
                    elif self.path.endswith('.png'):
                        self.send_header('Content-type', 'image/png')
                    elif self.path.endswith('.ico'):
                        self.send_header('Content-type', 'image/x-icon')
                    elif self.path.endswith('.css'):
                        self.send_header('Content-type', 'text/css')
                    else:
                        self.send_header('Content-type', 'application/octet-stream')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            # For any other path, redirect to setup page
            self.send_response(302)
            self.send_header('Location', 'http://192.168.4.1/')
            self.end_headers()

    def do_POST(self):
        if self.path == '/configure':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            
            ssid = params.get('ssid', [''])[0]
            password = params.get('password', [''])[0]
            
            if ssid and password:
                success = self.add_network_config(ssid, password)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"success": success, "message": "Konfiguration gespeichert. Gerät startet neu..."}
                self.wfile.write(json.dumps(response).encode())
                
                # Trigger restart after a short delay to ensure the response reaches the client
                if success:
                    threading.Timer(2.0, self.restart_system).start()
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"success": False, "message": "Ungültige Parameter"}
                self.wfile.write(json.dumps(response).encode())

    def scan_networks(self):
        try:
            scan_output = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan']).decode('utf-8')
            networks = []
            
            for line in scan_output.split('\n'):
                if 'ESSID:' in line:
                    essid = line.split('ESSID:')[1].strip('"')
                    if essid:  # Only add non-empty SSIDs
                        networks.append(essid)
            
            return sorted(list(set(networks)))  # Remove duplicates and sort
        except:
            return []

    def add_network_config(self, ssid, password):
        try:
            # Erstelle die komplette wpa_supplicant.conf
            config = f'''country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={{
    ssid="{ssid}"
    psk="{password}"
}}'''
            
            # Schreibe die Konfiguration mit sudo
            subprocess.run(['sudo', 'bash', '-c', f'echo \'{config}\' > /etc/wpa_supplicant/wpa_supplicant.conf'])
            subprocess.run(['sudo', 'chmod', '600', '/etc/wpa_supplicant/wpa_supplicant.conf'])
            
            # Erst jetzt die AP-Dienste deaktivieren
            subprocess.run(['sudo', 'systemctl', 'disable', 'hostapd'])
            subprocess.run(['sudo', 'systemctl', 'disable', 'dnsmasq'])
            subprocess.run(['sudo', 'systemctl', 'stop', 'hostapd'])
            subprocess.run(['sudo', 'systemctl', 'stop', 'dnsmasq'])
            
            # WLAN-Interface neu starten
            subprocess.run(['sudo', 'ifconfig', 'wlan0', 'down'])
            subprocess.run(['sudo', 'ifconfig', 'wlan0', 'up'])
            
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Netzwerkkonfiguration: {str(e)}")
            return False

    def restart_system(self):
        subprocess.run(['sudo', 'reboot'])

def setup_ap():
    """Setup Access Point mode"""
    try:
        # Stop wpa_supplicant temporarily
        subprocess.run(['sudo', 'systemctl', 'stop', 'wpa_supplicant'])
        subprocess.run(['sudo', 'systemctl', 'stop', 'networking'])
        
        # Enable and configure AP services
        subprocess.run(['sudo', 'systemctl', 'enable', 'hostapd'])
        subprocess.run(['sudo', 'systemctl', 'enable', 'dnsmasq'])
        
        # Configure hostapd
        hostapd_conf = '''interface=wlan0
driver=nl80211
ssid=GUSI-Radio Setup
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=12345
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP'''
        
        subprocess.run(['sudo', 'bash', '-c', f'echo \'{hostapd_conf}\' > /etc/hostapd/hostapd.conf'])
        
        # Configure dnsmasq for captive portal functionality
        dnsmasq_conf = '''interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
domain=wlan
address=/#/192.168.4.1'''
        
        subprocess.run(['sudo', 'bash', '-c', f'echo \'{dnsmasq_conf}\' > /etc/dnsmasq.conf'])
        
        # Configure network interface
        subprocess.run(['sudo', 'ifconfig', 'wlan0', '192.168.4.1', 'netmask', '255.255.255.0'])
        
        # Start services
        subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'])
        subprocess.run(['sudo', 'systemctl', 'start', 'dnsmasq'])
        
        # Reduzierte Wartezeit
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error in setup_ap: {str(e)}")
        return False

def main():
    # Setup Access Point
    max_retries = 3
    ap_started = False
    
    for attempt in range(max_retries):
        try:
            if setup_ap():
                ap_started = True
                break
            else:
                print(f"Attempt {attempt + 1} failed, retrying...")
                time.sleep(2)  # Reduzierte Wartezeit
        except Exception as e:
            print(f"Error during AP setup: {str(e)}")
            time.sleep(2)  # Reduzierte Wartezeit
    
    if not ap_started:
        print("Could not start Access Point, exiting...")
        return
    
    # Start web server
    server_address = ('', 80)
    httpd = HTTPServer(server_address, WifiSetupHandler)
    print("Server started at http://192.168.4.1")
    httpd.serve_forever()

if __name__ == '__main__':
    main()