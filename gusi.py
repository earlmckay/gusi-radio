import time
import os
import threading
from gpiozero import Button
from gpiozero import RotaryEncoder
from signal import pause
from subprocess import check_call
from urllib2 import Request, urlopen
from urllib2 import URLError, HTTPError

#---------- VAR DEFINITION ----------#
current_station = 0;
vol = 40;
btn_clk = RotaryEncoder(23, 27, bounce_time=float)
btn_sw = Button(22)
GODI = "http://mbgwaf.de:8000/stream"
DWG_DE = "https://server23644.streamplus.de/stream.mp3"
DWG_RU = "https://server32349.streamplus.de/stream.mp3"
SW_DE = "http://www.segenswelle.de:8000/deutsch"
SW_PD = "http://www.segenswelle.de:8000/plautdietsch"
SW_RU = "http://www.segenswelle.de:8000/russisch"

#---------- RADIO STATIONS ORDER ----------#
stations = [GODI, DWG_DE, DWG_RU, SW_DE, SW_PD, SW_RU]

#---------- ANNOUNCEMENTS ORDER ----------#
announcements = ["godi.mp3", "dwg_de.mp3", "dwg_ru.mp3", "sw_de.mp3", "sw_pd.mp3", "sw_ru.mp3"]

#---------- DEFINITIONS ----------#
def change_station():
    global current_station
    if timer is not None:
        timer.cancel()
    print("changing station from " + str(current_station))
    current_station = (current_station + 1) % len(stations)  
    play(current_station)

def play(current_station):
    print(stations[current_station])
    sudo_mpc("stop")
    sudo_mpc("clear")
    sudo_mpc("add " + announcements[current_station])
    if current_station == 0:
        sudo_mpc("add godi_offline.mp3")
        connect_godi()  
    else:
        sudo_mpc("add " + stations[current_station])
        sudo_mpc("play")
 
def connect_godi():
    global timer
    try:
        response = urlopen("http://mbgwaf.de:8000/stream")
    except:
        print('Godi ist offline')
        sudo_mpc("repeat on")
        sudo_mpc("play")
        #IN CASE OF TREAD PROBLEMS LOOK HERE#
        timer = threading.Timer(60, connect_godi)
        timer.start()  
    else:
        print('Godi ist online')
        sudo_mpc("clear")
        sudo_mpc("repeat off")
        sudo_mpc("add " + announcements[current_station])
        sudo_mpc("add " + stations[current_station])
        sudo_mpc("add godi_ended.mp3")
        sudo_mpc("play")

timer=None

def check_connection():
    try:
        response = urlopen("https://www.google.de")
    except:
        print('OFFLINE')
        sudo_mpc("add no_connection.mp3")
        sudo_mpc("add wps_client.mp3")
        sudo_mpc("play")
        time.sleep(10)
        btn_sw.wait_for_press(timeout=10)
        if btn_sw.is_pressed:
            sudo_mpc("clear")
            sudo_mpc("repeat off")
            sudo_mpc("add wps_router.mp3")
            sudo_mpc("play")
            time.sleep(13)
            os.system("sudo python /home/pi/gusi/auto_wps.py")   
        else:
            sudo_mpc("clear")
            sudo_mpc("repeat on")
            sudo_mpc("add problem.mp3")
            sudo_mpc("play")
            time.sleep(15)
            os.system("sudo python /home/pi/gusi/gusi.py")
    else:
        print('ONLINE')

def sudo_mpc(command):
    os.system("sudo mpc " + command)
    
def vol_up():
    global vol
    vol += 5
    print(str(vol))
    sudo_mpc("volume " + str(vol))

def vol_down():
    global vol
    vol -= 5
    print(str(vol))
    sudo_mpc("volume " + str(vol)) 
 
#---------- START ----------#
sudo_mpc("clear")
sudo_mpc("volume 40")
sudo_mpc("repeat off")
check_connection()
play(current_station)
 
btn_clk.when_rotated_clockwise = vol_up
btn_clk.when_rotated_counter_clockwise = vol_down
btn_sw.when_pressed = change_station


pause()
