import time
import os
import threading
from gpiozero import Button, RotaryEncoder, LED
from signal import pause
from subprocess import check_call, check_output
from urllib.request import urlopen

#---------- VAR DEFINITION ----------#
default_volume="/home/gusi/user_settings/default_volume.txt" # Set the default volume 
current_station = 0
shutdown_timer = None
shutdown_timeout = 60 * 60  # Time until auto off when paused or muted

# Lese gespeicherte Lautstärke oder nutze 30 als Standard
try:
    with open(default_volume, 'r') as f:
        vol = int(f.read().strip())
except:
    vol = 30

btn_clk = RotaryEncoder(23, 24, max_steps=4)
btn_sw = Button(22)
btn_play = Button(25)
led = LED(14)
S1 = "https://server7.streamserver24.com:61424/stream"
S2 = "http://www.segenswelle.de:8000/deutsch"
S3 = "https://server23644.streamplus.de/stream.mp3"

#---------- RADIO STATIONS ORDER ----------#
stations = [S1, S2, S3]

#---------- ANNOUNCEMENTS ORDER ----------#
announcements = ["s1.mp3", "s2.mp3", "s3.mp3"]

#---------- DEFINITIONS ----------#

# Store default volume
def save_default_volume():
    try:
        with open(default_volume, 'w') as f:
            f.write(str(vol))
        print(f"New standard volume of {vol} saved")
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
        led.on()
    except Exception as e:
        print(f"Error saving the new default volume: {e}")

# Save volume with a long press
def handle_rotary_button_press():
    start_time = time.time()
    while btn_sw.is_pressed:
        if time.time() - start_time >= 5:
            save_default_volume()
            return
        time.sleep(0.1)
    
    # Change station with a short press
    change_station()

# Status check for automatic shutdown
def check_and_set_timer():
    global shutdown_timer
    
    status = check_output(['mpc', 'status']).decode()
    volume = int(check_output(['mpc', 'volume']).decode().split(':')[1].strip().replace('%', ''))
    
    if shutdown_timer:
        shutdown_timer.cancel()
        shutdown_timer = None
    
    if '[paused]' in status or volume == 0:
        shutdown_timer = threading.Timer(shutdown_timeout, lambda: os.system("sudo shutdown -h now"))
        shutdown_timer.start()

def change_station():
    global current_station
    print("changing station from " + str(current_station))
    current_station = (current_station + 1) % len(stations)
    play(current_station)

def play(current_station):
    print(stations[current_station])
    os.system("mpc stop; mpc clear; mpc add " + announcements[current_station] + "; mpc add " + stations[current_station] + "; mpc play")
    check_and_set_timer()

def play_pause():
    os.system("mpc toggle")
    check_and_set_timer()

def vol_up():
    global vol
    if vol < 95:
        vol += 5
        if vol > 95:
            vol = 95
        print(str(vol))
        os.system("mpc volume " + str(vol))
        check_and_set_timer()

def vol_down():
    global vol
    if vol > 0:
        vol -= 5
        if vol < 0:
            vol = 0
        print(str(vol))
        os.system("mpc volume " + str(vol))
        check_and_set_timer()

#---------- START ----------#
led.on()
os.system("mpc clear; mpc repeat off; mpc volume " + str(vol))
play(current_station)

btn_clk.when_rotated_clockwise = vol_up
btn_clk.when_rotated_counter_clockwise = vol_down
btn_sw.when_pressed = handle_rotary_button_press
btn_play.when_pressed = play_pause

pause()