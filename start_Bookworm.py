import time
import subprocess
import re
from gpiozero import LED, Button

led = LED(14)
button = Button(22)
connection_attempts_local = 0
connection_attempts_internet = 0
connection_attempts_dhcp = 0

def check_internet_connection():
    global connection_attempts_internet
    print("Checking internet connection")
    while connection_attempts_internet < 4:
        print("Checking internet connection")
        try:
            subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])           
            print("Internet connection: true")
            return True
        except subprocess.CalledProcessError:
            print("Internet connection: false")
            connection_attempts_internet += 1
            time.sleep(5)
    return False

def check_local_network():
    global connection_attempts_local
    print("Checking local network")
    while connection_attempts_local < 4:
        print("Checking local connection")
        ret = subprocess.check_output(["ifconfig", "wlan0"]).decode("utf-8")
        reg = re.search("inet (\d+\.\d+\.\d+\.\d+)", ret)
        if reg is None:
            print("no IP found")
            connection_attempts_local += 1
            time.sleep(5)
        else:
            print("Local connection: true")
            return True
    return False

def check_DHCP_daemon():
    global connection_attempts_dhcp
    while connection_attempts_dhcp < 4:
        print("Checking NetworkManager service")
        dhcp_status = subprocess.call(["systemctl", "is-active", "NetworkManager"])
        if dhcp_status != 0:
            subprocess.call(["sudo", "systemctl", "start", "NetworkManager"])
            connection_attempts_dhcp += 1
            print("NetworkManager not started")
            time.sleep(5)
        else:
            print("NetworkManager is active")
            return True
    return False
    
def run_auto_wps_script():
    subprocess.call(["python3", "/home/gusi/gusi-radio/auto_wps.py"])
    quit()

def main():
    led.blink(on_time=0.6, off_time=0.6)
    
    # Check NetworkManager service
    if check_DHCP_daemon():

        # Check local network
        if check_local_network():

            # Local OK / internet OK
            if check_internet_connection():
                led.on()
                time.sleep(1)
                subprocess.Popen(["python3", "/home/gusi/gusi-radio/gusi.py"])
                quit()
            
            # Local OK / internet ERROR
            else:
                subprocess.call(["mpc", "clear"])
                subprocess.call(["mpc", "repeat", "off"])
                subprocess.call(["mpc", "add", "wifi_no_internet.mp3"])
                subprocess.call(["mpc", "play"])
                button.wait_for_press(timeout=30)
                if button.is_pressed:
                    led.on()
                    quit()
                subprocess.call(["sudo", "shutdown", "-h", "now"])
        
        # Local ERROR    
        else:
            subprocess.call(["mpc", "clear"])
            subprocess.call(["mpc", "repeat", "off"])
            subprocess.call(["mpc", "add", "wifi_no_router.mp3"])
            subprocess.call(["mpc", "add", "waiting.mp3"])
            subprocess.call(["mpc", "play"])
            led.blink(on_time=1, off_time=1)
            print("Wait for button press")
            button.wait_for_press(timeout=240)

            if button.is_pressed:
                led.on()
                subprocess.call(["mpc", "clear"])
                subprocess.call(["mpc", "repeat", "off"])
                subprocess.call(["mpc", "add", "wifi_wps_search.mp3"])
                subprocess.call(["mpc", "play"])
                time.sleep(12)
                run_auto_wps_script()
            
            print("Timeout: Button was not pressed")
            subprocess.call(["mpc", "clear"])
            subprocess.call(["mpc", "repeat", "off"])
            subprocess.call(["mpc", "add", "wifi_no_interaction.mp3"])
            subprocess.call(["mpc", "play"])
            time.sleep(40)
            subprocess.call(["sudo", "shutdown", "-h", "now"])


main()
