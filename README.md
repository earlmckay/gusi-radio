![](images/gusi-radio_panorama_3d.jpg)

# gusi-radio

GuSi – the user friendly internet radio

The GuSi radio is a very user-friendly internet radio with only two buttons. It allows the user to switch through predefined stations with just one push on the button. This makes it especially suitable for seniors or handicapped people.

------------

### Components you need

 - 1 x [Raspberry Pi zero](https://www.reichelt.de/de/de/raspberry-pi-zero-wh-v-1-1-1-ghz-512-mb-ram-wlan-bt-rasp-pi-zero-wh-p222531.html?&nbc=1)
 - 1 x [Power supply unit (5 V with a barrel jack 2.1 / 5.5 mm)](https://www.reichelt.de/de/de/steckernetzteil-12-w-5-v-2-4-a-ea1012ahes501-p293278.html?&nbc=1)
 - 1 x [Hifiberry MiniAMP](https://www.reichelt.de/de/de/raspberry-pi-shield-hifiberry-miniamp-rpi-hb-mini-amp-p191036.html?&nbc=1)
 - 1 x [Micro SD Card](https://www.reichelt.de/de/de/microsdhc-speicherkarte-16gb-sandisk-ultra-sdsquar016ggn6ma-p214843.html?&nbc=1)
 - 1 x [Small speaker with 10-30 W](https://www.reichelt.de/de/de/breitbandlautsprecher-fr-8-ta-10-w-4-ohm-vis-2402-p239748.html?&nbc=1)
 - 1 x [LED 5 mm](https://www.reichelt.de/de/de/led-5-mm-bedrahtet-kaltweiss-7150-mcd-50--led-el-5-7150kw-p164206.html?&nbc=1)
 - 1 x [Pushbuton (Cherry MX Key)](https://www.reichelt.de/de/de/cherry-mx-blue-keyswitch-cherry-mx1a-e1nn-p202569.html?&nbc=1)
 - 1 x [Power jack socket](https://www.reichelt.de/de/de/einbaubuchse-zentraleinbau-aussen-5-6-mm-innen-2-1-mm-hebl-21-p8524.html?&nbc=1)
 - 1 x [Speaker cable (about 0.5 mm²)](https://www.reichelt.de/de/de/zwillingslitze-flexibel-2x0-5mm-5m-ring-la-205-5-p9816.html?&nbc=1)
 - 1 x [Cable (about 0.14 mm²) for the connections](https://www.reichelt.de/de/de/kupferlitze-isoliert-10-m-1-x-0-14-mm-schwarz-litze-sw-p10298.html?&nbc=1)
 - 1 x [Micro-USB plug](https://www.reichelt.de/de/de/micro-usb-stecker-typ-b-5-polig-usb-micro-st-p124013.html?&nbc=1)
 - 6 x [Pan head screw M2.5 6 mm](https://www.ebay.de/itm/251411230965?_trkparms=ispr%3D1&hash=item3a8946f0f5:g:FYEAAOxydlFSrMWA&amdata=enc%3AAQAGAAACoPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSg3Ye8yTWgOW7pmE1t838dpsBclJk1M3ulJ%252FglBcTmXJX3%252BzRg0H2INadil%252BBp%252Fk%252BZY%252FI%252BR%252F5uJ0EoVAWur4JjuGs48Sg2KLeW%252BfF%252BaRPvEHQ%252BzfUq68tp6TKcf7bCp9xiAAHtK88EaOCE1ueldkUDYmH4i8crB%252FNoDd%252FMtRoHkRWLuQ9FRKNjTqua7zyMzCPcVT3KLCta8zEheq0RPYYOmW1KYRUcVc8eYGLXTMeVa34MfFfNdfN%252BJLqZ%252FhhrtV9OKFQBVq9rM%252BdgimLALmkp2xAwklhRJH1H56gfWjoghc5vMG%252BWp2FME5AeQVpADuWC4NRhHTI8E2GP2UI3426VWVQ9uDTMaJUJ6CMK%252Bgg2IAHQ8dNrA3CwlagbuB%252BGRI3r7vCTXbZx5zsRvjkw01GdeczQCdYotA4mJT6m3T9hXuC446gixqgCcNtCJgFHcsCZC2ai7Qfpq%252BmDMa1qJIU%252B4uXGY%252FV2qJ%252FNIkIldPFcwT7xgwRo0S9J72iEKf5tXg1HrZDxsTRWiYRuVDTdrnJP%252BudIqH%252BWO8YY15q4CSu8%252B72q5oVHwHFwDZGGdsRnCwRx3Zav9bpc9RcGap60Pxd8%252Bp4ZQC9uirkEFsw4lBKgdRFdYhK9MwP6aXsDw4SPjIIDSq%252F5uiRel%252BMiOHdVQwlR4L35UQMTlZDyR2QpdY%252FwbGfzO%252B%252BBo3RtbwAMmGnVGD3nx9aTrr2uwRYrrmjgXakt5l6IL3xSxt5IvMYZE%252BO6gBad9VLLtI4np1qGjoLGWHx35NqyfM45ATQvCoV6Yu4xOaQVz%252FNVph4NcoSQ1RVz%252Fm4TdMZrDx%252FscbNagSiyy1JZUXA6Z0GmcfdOqJ1ItIFsQ%253D%253D%7Cclp%3A2334524%7Ctkp%3ABFBMyJyE5c1f)
 - 6 x [Pan head screw M2.5 10 mm](https://www.ebay.de/itm/251411230965?_trkparms=ispr%3D1&hash=item3a8946f0f5:g:FYEAAOxydlFSrMWA&amdata=enc%3AAQAGAAACoPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSg3Ye8yTWgOW7pmE1t838dpsBclJk1M3ulJ%252FglBcTmXJX3%252BzRg0H2INadil%252BBp%252Fk%252BZY%252FI%252BR%252F5uJ0EoVAWur4JjuGs48Sg2KLeW%252BfF%252BaRPvEHQ%252BzfUq68tp6TKcf7bCp9xiAAHtK88EaOCE1ueldkUDYmH4i8crB%252FNoDd%252FMtRoHkRWLuQ9FRKNjTqua7zyMzCPcVT3KLCta8zEheq0RPYYOmW1KYRUcVc8eYGLXTMeVa34MfFfNdfN%252BJLqZ%252FhhrtV9OKFQBVq9rM%252BdgimLALmkp2xAwklhRJH1H56gfWjoghc5vMG%252BWp2FME5AeQVpADuWC4NRhHTI8E2GP2UI3426VWVQ9uDTMaJUJ6CMK%252Bgg2IAHQ8dNrA3CwlagbuB%252BGRI3r7vCTXbZx5zsRvjkw01GdeczQCdYotA4mJT6m3T9hXuC446gixqgCcNtCJgFHcsCZC2ai7Qfpq%252BmDMa1qJIU%252B4uXGY%252FV2qJ%252FNIkIldPFcwT7xgwRo0S9J72iEKf5tXg1HrZDxsTRWiYRuVDTdrnJP%252BudIqH%252BWO8YY15q4CSu8%252B72q5oVHwHFwDZGGdsRnCwRx3Zav9bpc9RcGap60Pxd8%252Bp4ZQC9uirkEFsw4lBKgdRFdYhK9MwP6aXsDw4SPjIIDSq%252F5uiRel%252BMiOHdVQwlR4L35UQMTlZDyR2QpdY%252FwbGfzO%252B%252BBo3RtbwAMmGnVGD3nx9aTrr2uwRYrrmjgXakt5l6IL3xSxt5IvMYZE%252BO6gBad9VLLtI4np1qGjoLGWHx35NqyfM45ATQvCoV6Yu4xOaQVz%252FNVph4NcoSQ1RVz%252Fm4TdMZrDx%252FscbNagSiyy1JZUXA6Z0GmcfdOqJ1ItIFsQ%253D%253D%7Cclp%3A2334524%7Ctkp%3ABFBMyJyE5c1f)
 - 1 x [GPIO edge adapter](https://www.berrybase.de/neu/gpio-edge-erweiterung-gpio-adapter-f-252-r-raspberry-pi?c=2413)
 - Some [Dupont crimps](https://www.reichelt.de/de/de/entwicklerboards-dupont-crimp-set-610-teilig-debo-set-dupont-p279901.html?&nbc=1)
 - 1 x [Rotarry encoder KY-040](https://www.berrybase.de/bauelemente/passive-bauelemente/potentiometer/drehimpulsgeber/drehregler/rotary-encoder-mit-breakoutboard)
 - 1 x [SHIM OnOff](https://www.reichelt.de/de/de/raspberry-pi-shield-onoff-shim-rpi-shd-onoff-p272023.html?&nbc=1)

80% of the components can be purchased from reichelt.de (Preconfigured shopping cart: [Gusi Radio](https://www.reichelt.de/my/1832192 "Gusi Radio")). The screws, the GPIO edge and the Rotary Encoder are not available there.

The 3D data can be downloaded [here](https://www.thingiverse.com/thing:4823464 "Thingiverse").

------------

### Software installation

 **1) Install the OS**
 Install Raspberry Pi OS lite on the SD card. You can use the tool [Raspberry Pi imager](https://www.raspberrypi.org/software/ "Raspberry Pi imager") for this.

  **2) Prepare the SD-Card**
After the installation, open the SD card (should be labeled as "boot") and copy the files from the folder "sd-card" to the card.
- *ssh* (allows to connect via ssh)
- *wpa_supplicant.conf* (WiFi connection)


Open the *config.txt* with an editor. Add the following code at the bottom:
```
 ################## GUSI ################
# Disable Bluetooth`
dtoverlay=pi3-disable-bt
# Power On/Off Button
dtoverlay=gpio-shutdown,gpio_pin=3, active_low=1,gpio_pull=up
# Enable Hifiberry Soundcard
dtoverlay=hifiberry-dac
```

Open the *wpa_supplicant.conf*  and enter the WiFi access data there.

------------


  **3) SSH Connection**
Insert the card into the Raspberry and let it boot up. Find out which IP address your Pi got. Now access the Raspberry via SSH.

`ssh pi@192.168.1.100`

The default login data are "pi" and "raspberry"

------------


  **4) Raspberry Configuration**
Change device name:

`hostnamectl set-hostname 'GuSi'`

Change password:

`passwd`

Change time zone:

`sudo timedatectl set-timezone Europe/Berlin`

------------

  **5) Install SHIM OnOFF**

`curl https://get.pimoroni.com/onoffshim | bash`

------------

  **6) Set up Hifiberry**
Set Hifiberry as default audio device

`sudo nano /etc/asound.conf`

Insert following text:
```
pcm.hifiberryMiniAmp {
    type softvol
    slave.pcm "plughw:0"
    control.name "Master"
    control.card 0
}
pcm.!default {
    type       plug
    slave.pcm  "hifiberryMiniAmp"
}
```

------------


  **7) Install Music Player Deamon**
  
`sudo apt-get update`

`sudo apt-get upgrade`

`sudo apt-get install mpd mpc alsa-utils`

Improve stability:

`sudo nano /etc/modprobe.d/8192cu.conf`

Insert following text:
```
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0

rtw_ips_mode=1

```

------------

  **8) Install GuSi**

Install git:

`sudo apt install git`

Clone the repository:

`git clone https://github.com/earlmckay/gusi-radio`

Replace the original MPC config:

`sudo mv /home/pi/gusi-radio/mpd.conf /etc/`

Replace the original cleanshutd Config:

`sudo mv /home/pi/gusi-radio/cleanshutd.conf /etc/`

Reboot the device

`sudo reboot`

Update the Music player database

`sudo mpc update`

------------


  **9) Set up autostart**

`crontab -e`

Insert following text at the bottom:
```
@reboot /home/pi/gusi-radio/autostart.sh
```

Make the scripts executable:

`sudo chmod a+x /home/pi/gusi-radio/autostart.sh`
`sudo chmod a+x /home/pi/gusi-radio/auto_wps.py`

------------


  **10) Install Python 3 librarys**

sudo apt-get install python3-pip`

`sudo apt install python3-gpiozero`


------------

  **11) Customize the Code**

sudo nano /home/pi/gusi-radio/gusi.py`

Open the file "gusi.py" and adjust the URLs in the variables (GODI, DWG ...).
You can run the script with the command:

`python3 /home/pi/gusi-radio/gusi.py`

------------


  **12) Optimization**
Deaktivate swapping:

`sudo systemctl stop dphys-swapfile`

`sudo systemctl disable dphys-swapfile`

Deactivate some unused modules:

`sudo systemctl disable keyboard-setup.service`

`sudo systemctl disable triggerhappy.service`

`sudo /usr/bin/tvservice -o`

Reboot the device

`sudo reboot`

------------

## Hardware installation

Solder the micro USB cable to the power socket and screw it into the case. Also the raspberry. 
![](images/step_1.jpg)

Screw the speaker to the mount, solder the cables to it and connect it to the amplifier.
![](images/step_2.jpg)

Solder cables to the push button, rotary encoder and the LED. Between LED and cable is the resistor.
![](images/step_3.jpg)

Screw the rotary encoder and the pushbutton into the housing. Slide the speaker holder into the slot.
![](images/step_4.jpg)

Insert the LED into the hole. You can fix this with hot glue.
![](images/step_5.jpg)

Connect the cable ends to the Raspberry. 
| Pin | Physical | BCM |
| :------------ | :------------: | :------------: |
| Rotary CLK | 11 | 17 |
| Rotary DT | 13 | 27 |
| Rotary SW | 15 | 22 |
| Rotary 3V | 17 |
| Rotary GND | 14 |
| Power | 5 | 3 |
| Power | 9 |
| LED + | 8 | 14 |
| LED GND | 20 |

![](images/routing.jpg)

Insert the bass reflex tube into the hole on the the back.
![](images/step_6.jpg)

Close the housing and screw it with 4 screws.
![](images/step_7.jpg)

------------
Finally, I would like to thank [Robert Nickel](https://github.com/Robert-Nickel) for his support, as well to [Notification Sounds](https://notificationsounds.com/) for providing the sounds.
