import time
import os
import threading
from gpiozero import Button, RotaryEncoder, LED
from signal import pause
from subprocess import check_call
from urllib.request import urlopen

#---------- VAR DEFINITION ----------#
current_station = 0
vol = 30
btn_clk = RotaryEncoder(23, 27, max_steps=4)
btn_sw = Button(22)
led = LED(14)
S1 = "https://server7.streamserver24.com:61424/stream"
S2 = "http://www.segenswelle.de:8000/deutsch"
S3 = "https://server23644.streamplus.de/stream.mp3"

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
    os.system("mpc stop; mpc clear; mpc add " + announcements[current_station] + "; mpc add " + stations[current_station] + "; mpc play")

def vol_up():
    global vol
    if vol < 95:
        vol += 5
        if vol > 95:
            vol = 95
        print(str(vol))
        os.system("mpc volume " + str(vol))

def vol_down():
    global vol
    if vol > 0:
        vol -= 5
        if vol < 0:
            vol = 0
        print(str(vol))
        os.system("mpc volume " + str(vol))

#---------- START ----------#
led.on()
os.system("mpc clear; mpc repeat off; mpc volume " + str(vol))
play(current_station)

btn_clk.when_rotated_clockwise = vol_up
btn_clk.when_rotated_counter_clockwise = vol_down
btn_sw.when_pressed = change_station

pause()
