import re
import subprocess
import time
import os
from gpiozero import LED

led = LED(14)

def checkip():
    print("Check IP")
    ret = subprocess.check_output(["ifconfig", "wlan0"]).decode("utf-8")
    reg = re.search("inet (\d+\.\d+\.\d+\.\d+)", ret)
    if reg is None:
        print("No IP in ifconfig")
        return False
    else:
        print("Found IP in ifconfig")
        return reg.group(1)

##########     START     ##########

led.blink(on_time=0.3, off_time=0.3)
subprocess.call(["mpc", "clear"])
subprocess.call(["mpc", "repeat", "on"])
subprocess.call(["mpc", "add", "wifi_ping.mp3"])
subprocess.call(["mpc", "play"])

print("STOP wpa_supplicant")
subprocess.run(["sudo", "killall", "-q", "wpa_supplicant"])
time.sleep(3)

print("reset wpa_supplicant.conf")
new_config = """ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DE
"""
with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
    f.write(new_config)
time.sleep(5)

print("START wpa_supplicant")
subprocess.run(["sudo", "wpa_supplicant", "-B", "-i", "wlan0", "-c", "/etc/wpa_supplicant/wpa_supplicant.conf"])

ip = checkip()
connection_attempts = 0

while connection_attempts < 4:
    # no IP address, so start looking for WPS-PBC network
    if ip is False:
        connection_attempts += 1
    
        # scan networks on interface wlan0, to see some nice networks
        print("scanning network")
        subprocess.check_output(["wpa_cli", "-i", "wlan0", "scan"])
        time.sleep(1)
        
        #get and decode results
        print("get result")
        wpa = subprocess.check_output(["wpa_cli", "-i", "wlan0", "scan_results"]).decode("UTF-8")
        time.sleep(3)

        #parse response to get MAC address of router that has WPS-PBC state
        print("MAC address")
        active_spot_reg = re.search("(([\da-f]{2}:){5}[\da-f]{2})(.*?)\[WPS-PBC\]", wpa)
        print("MAC address", active_spot_reg)
        
        #check if we found any 
        print("check catch")
        if not (active_spot_reg is None):
            if active_spot_reg.group(1):
                
                #connect via wps_pbc
                subprocess.check_output(["wpa_cli", "-i", "wlan0", "wps_pbc", active_spot_reg.group(1)])
                
                # some debug
                print("MAC address:", active_spot_reg.group(1))
                print(active_spot_reg.group(1))
                print(wpa)
                time.sleep(5)

                led.on()

                print("STOP wpa_supplicant")
                subprocess.run(["sudo", "killall", "-q", "wpa_supplicant"])
                time.sleep(3)

                print("START wpa_supplicant")
                subprocess.run(["sudo", "wpa_supplicant", "-B", "-i", "wlan0", "-c", "/etc/wpa_supplicant/wpa_supplicant.conf"])

                print("Success!")
                subprocess.call(["mpc", "clear"])
                subprocess.call(["mpc", "add", "wifi_wps_successful.mp3"])
                subprocess.call(["mpc", "play"])
                subprocess.call(["mpc", "repeat", "off"])
                time.sleep(26)
                os.system("python3 /home/gusi/gusi-radio/gusi.py")
                quit()
                break
        
    # sleep to scan again
    time.sleep(10)

else:
    led.blink(on_time=0.6, off_time=0.6)
    print("Network is not up")
    print("IP address:", ip)
    subprocess.call(["mpc", "clear"])
    subprocess.call(["mpc", "add", "wifi_wps_fail.mp3"])
    subprocess.call(["mpc", "play"])
    subprocess.call(["mpc", "repeat", "off"])
    time.sleep(45)
    os.system("sudo shutdown now")