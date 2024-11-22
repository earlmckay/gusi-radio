import time
import subprocess
import re
import socket
from datetime import datetime
from gpiozero import LED, Button

led = LED(14)
button = Button(22)
connection_attempts_local = 0
connection_attempts_internet = 0
connection_attempts_dhcp = 0

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def get_network_info():
    """Collects detailed network information"""
    info = {}
    try:
        # WLAN Interface Status
        wlan_output = subprocess.check_output(["iwconfig", "wlan0"]).decode("utf-8")
        info["ssid"] = re.search('ESSID:"([^"]*)"', wlan_output)
        info["ssid"] = info["ssid"].group(1) if info["ssid"] else "Not connected"
        info["signal"] = re.search("Signal level=([0-9-]+)", wlan_output)
        info["signal"] = info["signal"].group(1) if info["signal"] else "Unknown"
        
        # IP Configuration
        ifconfig_output = subprocess.check_output(["ifconfig", "wlan0"]).decode("utf-8")
        ip_match = re.search("inet (\d+\.\d+\.\d+\.\d+)", ifconfig_output)
        info["ip"] = ip_match.group(1) if ip_match else "No IP"
        
        # Gateway Information
        route_output = subprocess.check_output(["ip", "route"]).decode("utf-8")
        default_gw = re.search("default via (\d+\.\d+\.\d+\.\d+)", route_output)
        info["gateway"] = default_gw.group(1) if default_gw else "No Gateway"
        
        # DNS Server
        with open("/etc/resolv.conf", "r") as f:
            resolv_conf = f.read()
        dns_servers = re.findall("nameserver\s+(\d+\.\d+\.\d+\.\d+)", resolv_conf)
        info["dns_servers"] = dns_servers if dns_servers else ["No DNS Servers"]
        
    except Exception as e:
        log_message(f"Error collecting network information: {str(e)}")
        return None
    
    return info

def check_internet_connection():
    """
    Check internet connectivity using DNS resolution and ping
    Returns True if connection is established, False otherwise
    """
    global connection_attempts_internet
    log_message("Checking internet connection...")
    
    while connection_attempts_internet < 4:
        try:
            # Test DNS resolution
            try:
                socket.gethostbyname("google.com")
                log_message("DNS Resolution: Successful")
            except socket.gaierror:
                log_message("DNS Resolution: Failed")
            
            # Ping test to Google DNS
            subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])           
            log_message("Internet Connection: OK")
            return True
        except subprocess.CalledProcessError:
            log_message(f"Internet Connection: Failed (Attempt {connection_attempts_internet + 1}/4)")
            connection_attempts_internet += 1
            time.sleep(5)
    return False

def check_local_network():
    """
    Check local network connectivity and collect network information
    Returns True if local connection is established, False otherwise
    """
    global connection_attempts_local
    log_message("Checking local network...")
    
    while connection_attempts_local < 4:
        network_info = get_network_info()
        if network_info:
            log_message(f"""
Network Status:
- SSID: {network_info['ssid']}
- Signal Strength: {network_info['signal']} dBm
- IP Address: {network_info['ip']}
- Gateway: {network_info['gateway']}
- DNS Servers: {', '.join(network_info['dns_servers'])}
""")
            
            if network_info['ip'] != "No IP":
                log_message("Local Connection: OK")
                return True
        
        log_message(f"No IP address found (Attempt {connection_attempts_local + 1}/4)")
        connection_attempts_local += 1
        time.sleep(8)
    return False

def check_DHCP_daemon():
    """
    Check and restart DHCP service if necessary
    Returns True if service is running, False after max attempts
    """
    global connection_attempts_dhcp
    while connection_attempts_dhcp < 4:
        log_message("Checking DHCP service...")
        dhcp_status = subprocess.call(["systemctl", "is-active", "dhcpcd"])
        
        if dhcp_status != 0:
            log_message("DHCP Service not active, restarting...")
            subprocess.call(["sudo", "systemctl", "restart", "dhcpcd"])
            connection_attempts_dhcp += 1
            time.sleep(5)
        else:
            log_message("DHCP Service: OK")
            return True
    return False

def run_auto_wps_script():
    """Start the WPS configuration script"""
    log_message("Starting WPS script...")
    subprocess.Popen(["python3", "/home/gusi/gusi-radio/auto_wps.py"])
    quit()

def main():
    """
    Main function controlling the network connection flow:
    1. Check DHCP service
    2. Check local network connection
    3. Check internet connection
    4. Handle various error cases with audio feedback
    """
    log_message("=== Starting Network Diagnostics ===")
    led.blink(on_time=0.6, off_time=0.6)
    
    if check_DHCP_daemon():
        if check_local_network():
            if check_internet_connection():
                led.on()
                time.sleep(1)
                log_message("All checks successful, starting radio...")
                subprocess.Popen(["python3", "/home/gusi/gusi-radio/gusi.py"])
                quit()
            else:
                log_message("No internet despite local connection")
                subprocess.call(["mpc", "clear"])
                subprocess.call(["mpc", "repeat", "off"])
                subprocess.call(["mpc", "add", "wifi_no_internet.mp3"])
                subprocess.call(["mpc", "play"])
                log_message("Waiting for button press...")
                button.wait_for_press(timeout=60)
                if button.is_pressed:
                    led.on()
                    subprocess.call(["mpc", "clear"])
                    subprocess.call(["mpc", "repeat", "off"])
                    subprocess.call(["mpc", "add", "wifi_wps_search.mp3"])
                    subprocess.call(["mpc", "play"])
                    time.sleep(12)
                    run_auto_wps_script()
                subprocess.call(["sudo", "shutdown", "-h", "now"])
        else:
            log_message("No local network connection")
            subprocess.call(["mpc", "clear"])
            subprocess.call(["mpc", "repeat", "off"])
            subprocess.call(["mpc", "add", "wifi_no_router.mp3"])
            subprocess.call(["mpc", "add", "waiting.mp3"])
            subprocess.call(["mpc", "play"])
            led.blink(on_time=1, off_time=1)
            log_message("Waiting for button press...")
            button.wait_for_press(timeout=240)

            if button.is_pressed:
                led.on()
                subprocess.call(["mpc", "clear"])
                subprocess.call(["mpc", "repeat", "off"])
                subprocess.call(["mpc", "add", "wifi_wps_search.mp3"])
                subprocess.call(["mpc", "play"])
                time.sleep(12)
                run_auto_wps_script()
            
            log_message("Timeout: No user interaction")
            subprocess.call(["mpc", "clear"])
            subprocess.call(["mpc", "repeat", "off"])
            subprocess.call(["mpc", "add", "wifi_no_interaction.mp3"])
            subprocess.call(["mpc", "play"])
            time.sleep(40)
            subprocess.call(["sudo", "shutdown", "-h", "now"])

if __name__ == "__main__":
    main()