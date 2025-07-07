import time
import os
import threading
from gpiozero import Button, RotaryEncoder, LED
from signal import pause
from subprocess import check_call, check_output
from urllib.request import urlopen

#---------- VAR DEFINITION ----------#
# Set the default volume 
default_volume="/home/gusi/gusi-radio/user_settings/default_volume.txt" 
connection_timer = None
shutdown_timer = None
shutdown_timeout = 60 * 60  # Time until auto off when paused or muted

# Reading default volume
try:
    with open(default_volume, 'r') as f:
        vol = int(f.read().strip())
except:
    vol = 30

btn_clk = RotaryEncoder(23, 24, max_steps=4)
btn_sw = Button(22)
btn_s1 = Button(12)
btn_s2 = Button(5)
btn_s3 = Button(6)
btn_s4 = Button(13)
led = LED(14)
GODI_WAF = "http://mbgwaf.de:8000/stream"
DWG_DE = "https://server23644.streamplus.de/stream.mp3"
SW_RU = "http://www.segenswelle.de:8000/russisch"
SW_DE = "http://www.segenswelle.de:8000/deutsch"

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
    
    # Play/Pause with a short press
    play_pause()

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

def connect_godi():
    global connection_timer
    try:
        response = urlopen(GODI_WAF)
    except:
        print('Godi ist offline')
        os.system("mpc repeat on; mpc play")
        connection_timer = threading.Timer(60, connect_godi)
        connection_timer.start()
    else:
        print('Godi ist online')
        os.system("mpc clear; mpc repeat off; mpc add godi_warendorf.mp3; mpc add " + GODI_WAF + "; mpc add godi_ended.mp3; mpc play")
        check_and_set_timer()

def play_station_1():
    print("Playing station 1")
    global connection_timer
    if connection_timer is not None:
        connection_timer.cancel()
        connection_timer = None 
    os.system("mpc stop; mpc clear; mpc add godi_offline.mp3")
    connect_godi()

def play_station_2():
    print("Playing station 2")
    global connection_timer
    if connection_timer is not None:
        connection_timer.cancel()
        connection_timer = None    
    os.system("mpc stop; mpc clear; mpc add dwg_de.mp3; mpc add " + DWG_DE + "; mpc play")
    check_and_set_timer()

def play_station_3():
    print("Playing station 3")
    global connection_timer
    if connection_timer is not None:
        connection_timer.cancel()
        connection_timer = None    
    os.system("mpc stop; mpc clear; mpc add sw_ru.mp3; mpc add " + SW_RU + "; mpc play")
    check_and_set_timer()

def play_station_4():
    print("Playing station 4")
    global connection_timer
    if connection_timer is not None:
        connection_timer.cancel()
        connection_timer = None    
    os.system("mpc stop; mpc clear; mpc add sw_de.mp3; mpc add " + SW_DE + "; mpc play")
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
play_station_1()

btn_clk.when_rotated_clockwise = vol_up
btn_clk.when_rotated_counter_clockwise = vol_down
btn_sw.when_pressed = handle_rotary_button_press
btn_s1.when_pressed = play_station_1
btn_s2.when_pressed = play_station_2
btn_s3.when_pressed = play_station_3
btn_s4.when_pressed = play_station_4

pause()