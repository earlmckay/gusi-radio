import re
import subprocess
import time
import os

def checkip():
    # here is a little function that can tell me if my rpi has IP address and wat it is
    ret = subprocess.check_output(["ifconfig", "wlan0"]).decode("utf-8")
    reg = re.search("inet (\d+\.\d+\.\d+\.\d+)", ret)
    if reg is None:
        print("no ip found")
        return False
    else:
        return reg.group(1)

ip = checkip()
count = 1

os.system("sudo mpc clear")
os.system("sudo mpc repeat on")
os.system("sudo mpc add wps_ping.mp3")
os.system("sudo mpc play")

#run until we are sure that WiFi is connected and running
while 1:
    # no IP address, so start looking for WPS-PBC network
    if ip is False and count < 11:

        # limiting the scan to 5 rounds (add 1)
        count += 1

        # scan networks on interface wlan0, to see some nice networks
        print("scanning network")
        subprocess.check_output(["wpa_cli", "-i", "wlan0", "scan"])

        #works better with some sleep, dunno why
        print("sleep for 2 secounds")
        time.sleep(2);

        #get and decode results
        print("get result")
        wpa = subprocess.check_output(["wpa_cli", "-i", "wlan0", "scan_results"]).decode("UTF-8")

        #parse response to get MAC address of router that has WPS-PBC state
        print("get MAC address")
        active_spot_reg = re.search("(([\da-f]{2}:){5}[\da-f]{2})(.*?)\[WPS-PBC\]", wpa)

        #check if we found any
        if not (active_spot_reg is None):
            if active_spot_reg.group(1):

                #connect via wps_pbc
                subprocess.check_output(["wpa_cli", "-i", "wlan0", "wps_pbc", active_spot_reg.group(1)])

                # some debug
                print(active_spot_reg.group(1))
                print(wpa)
                os.system("sudo mpc clear")
                os.system("sudo mpc repeat off")
                os.system("sudo mpc add wps_successfull.mp3")
                os.system("sudo mpc play")
                time.sleep(8)
                os.system("sudo reboot")
    else:
        print("network is up")
        os.system("sudo mpc clear")
        os.system("sudo mpc add wps_error.mp3")
        os.system("sudo mpc play")
        time.sleep(12)
        os.system("sudo shutdown now")
        break

    # sleep to scan again
    time.sleep(10)
