import time
import os
from gpiozero import Button
from gpiozero import RotaryEncoder
from signal import pause
from subprocess import check_call
import urllib
from urllib.request import Request, urlopen

#---------- VAR DEFINITION ----------#
current_station = 0
vol = 34
btn_clk = RotaryEncoder(23, 27, bounce_time=float)
btn_sw = Button(22)
S1 = "http://www.segenswelle.de:8000/deutsch"
S2 = "https://server23644.streamplus.de/stream.mp3"
S3 = "https://server32349.streamplus.de/stream.mp3"

#---------- RADIO STATIONS ORDER ----------#
stations = [S1, S2, S3]

#---------- ANNOUNCEMENTS ORDER ----------#
announcements = ["s1.mp3", "s2.mp3", "s3.mp3"]

#---------- DEFINITIONS ----------#
def change_station():
    global current_station
    print("changing station from " + str(current_station))
    current_station = (current_station + 1) % len(stations)
    play(current_station)

def play(current_station):
    print(stations[current_station])
    os.system("mpc clear; mpc add " + announcements[current_station] + "; mpc add " + stations[current_station] + "; mpc play")

def check_connection():

    offline_count = 1

    try:
        response = urlopen("https://www.google.de")
    except:
        while offline_count < 4:
            print("Ckeck connection " , offline_count)
            time.sleep(5)
            offline_count += 1
        else:
            print('OFFLINE')
            os.system("mpc clear; mpc repeat off; mpc add no_connection.mp3; mpc add wps_client.mp3; mpc play")
            btn_sw.wait_for_press(timeout=40)
            if btn_sw.is_pressed:
                os.system("mpc clear; mpc add wps_router.mp3; mpc play")
                time.sleep(16)
                os.system("sudo python3 /home/gusi/gusi-radio/auto_wps.py")
                quit()

            os.system("mpc clear; mpc add wps_error.mp3; mpc play")
            time.sleep(21)
            os.system("sudo shutdown now")
    else:
        print('ONLINE')

def vol_up():
    global vol
    vol += 2
    print(str(vol))
    os.system("mpc volume " + str(vol))

def vol_down():
    global vol
    vol -= 2
    print(str(vol))
    os.system("mpc volume " + str(vol))

#---------- START ----------#
os.system("mpc clear; mpc repeat off; mpc volume 34")
check_connection()
play(current_station)

btn_clk.when_rotated_clockwise = vol_up
btn_clk.when_rotated_counter_clockwise = vol_down
btn_sw.when_pressed = change_station


pause()
