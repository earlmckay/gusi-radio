<img src="images/thumbnail.jpg">


<h1>GuSi-Radio</h1>

GuSi – the user friendly internet radio

The GuSi radio is a very user-friendly internet radio with only two buttons. It allows the user to switch through predefined stations with just one push on the button. This makes it especially suitable for seniors or handicapped people.

A short demonstration of the radio:

[![Functionality](https://img.youtube.com/vi/FBuoywtGWyI/0.jpg)](https://youtu.be/FBuoywtGWyI)

------------
</br>
<div class="warning" style='padding:1em; background-color:#F1C40F; color:black'>
<span>
<p style='text-align:center'>
<img src="images/flag_de.svg" alt=(DE) style="width:16px"> <b>WLAN-Anmeldung ohne WPS</b></p>
Öffne das Gehäuse, entnehme die SD-Karte und stecke diese in einen Computer. Öffne den Text-Editor und füge folgenden Code ein:

```
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="NAME"
psk="KENNWORT"
}
```

Ersetze <b>NAME</b> und <b>KENNWORT</b> innerhalb der Anführungszeichen durch die WLAN-Anmeldedaten ersetzen.

Speicher das Dokument als Datei speichern als: wpa_supplicant.conf
Achte darauf, dass die Endung ".conf" sein muss und nicht ".txt"!

Datei auf die SD-Karte einfügen, zurück ins Radio setzen und starten.
</div>
<br>
<div class="warning" style='padding:1em; background-color:#F1C40F; color:black'>
<span>
<p style='text-align:center'>
<img src="images/flag_en.svg" alt=(DE) style="width:16px"> <b>WiFi registration without WPS</b></p>
Open the housing, remove the SD card and insert it into a computer. Open the text editor and insert the following code:

```
country=EN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="NAME"
psk="KENNWORT"
}
```

Replace <b>NAME</b> and <b>PASSWORD</b> within the quotation marks with the WiFi credentials.

Save the document as a file Save as:  wpa_supplicant.conf
Make sure that the extension is “.conf” and not “.txt”!

Move the file onto the SD-card, put it back into the radio and start it.
</div>
</br>

<hr>

<h3 style='color: #16A085; font-size: 2em;'><img src="images/icon_parts.svg" alt=(DE) style="height:22px"> Part list</h3>

<ul>
  <li> 1 x <a href="https://www.reichelt.de/raspberry-pi-zero-2-w-4x-1-ghz-512-mb-ram-wlan-bt-rasp-pi-zero2-w-p313902.html?&nbc=1">Raspberry Pi zero</a>
  
  <li> 1 x <a href="https://www.reichelt.de/raspberry-pi-gpio-header-40-polig-rm-2-54-farblich-kodiert-rpi-header-cg3-p283342.html?&nbc=1">Raspberry Header CG3</a>
  
  <li> 1 x <a href="https://www.reichelt.de/steckernetzteil-12-w-5-v-2-4-a-ea1012ahes501-p293278.html?&nbc=1">Power supply unit (5 V with a barrel jack 2.1 / 5.5 mm)</a>
 
  <li> 1 x <a href="https://www.reichelt.de/raspberry-pi-shield-hifiberry-miniamp-rpi-hb-mini-amp-p191036.html?&nbc=1">Hifiberry MiniAMP</a>
  
  <li> 1 x <a href="https://www.reichelt.de/microsdhc-speicherkarte-32gb-sandisk-ultra-sdsqua4032ggn6ma-p297179.html?&nbc=1">Micro SD Card</a>
  
  <li> 1 x <a href="(https://www.reichelt.de/breitbandlautsprecher-fr-8-ta-10-w-4-ohm-vis-2402-p239748.html?&nbc=1">Small speaker with 10-30 W</a>
  
  <li> 1 x <a href="https://www.reichelt.de/led-5-mm-bedrahtet-kaltweiss-7150-mcd-50--led-el-5-7150kw-p164206.html?&nbc=1">LED 5 mm</a>
  
  <li> 1 x <a href="https://www.reichelt.de/cherry-mx-blue-tastenmodul-schnappbefestigung-cherry-mx1a-e1nn-p202569.html?&nbc=1">Pushbuton (Cherry MX Key)</a>
  
  <li> 1 x <a href="https://www.reichelt.de/einbaubuchse-zentraleinbau-aussen-5-6-mm-innen-2-1-mm-hebl-21-p8524.html?&nbc=1">Power jack socket</a>
  
  <li> 1 x <a href="https://www.reichelt.de/lautsprecherkabel-rot-schwarz-cu-10-m-la-205-10-p9813.html?&nbc=1">Speaker cable (about 0.5 mm²</a>

  <li> 1 x <a href="https://www.reichelt.de/kupferlitze-isoliert-10-m-1-x-0-14-mm-schwarz-litze-sw-p10298.html?&nbc=1">Cable (about 0.14 mm²)</a>

  <li> 1 x <a href="https://www.reichelt.de/micro-usb-stecker-typ-b-5-polig-usb-micro-st-p124013.html?&nbc=1">Micro-USB plug</a>

  <li> 1 x <a href="url">Pan head screw M2.5 6 mm</a>

  <li> 1 x <a href="url">Pan head screw M2.5 10 mm</a>

  <li> 1 x <a href="https://www.reichelt.de/raspberry-pi-gpio-header-1-auf-2-40-polig-rm-2-54-rpi-gpio-1to2-p276993.html?&nbc=1">GPIO edge adapter</a>

  <li> 1 x <a href="https://www.reichelt.de/entwicklerboards-dupont-crimp-set-610-teilig-debo-set-dupont-p279901.html?&nbc=1">Dupont crimps set</a>

  <li> 1 x <a href="https://www.reichelt.de/entwicklerboards-drehwinkel-encoder-ky-040-debo-encoder-p282545.html?&nbc=1">Rotarry encoder KY-040</a>

  <li> 1 x <a href="https://www.reichelt.de/raspberry-pi-shield-onoff-shim-rpi-shd-onoff-p272023.html?&nbc=1">SHIM OnOff</a>
</ul>

Almost everything except the screws can be ordered via this  <a href="https://www.reichelt.de/my/2179350">part list</a>. 

<hr>

<h3 style='color: #16A085; font-size: 2em;'><img src="images/icon_print.svg" alt=(DE) style="height:22px"> 3D-Print files</h3>

The 3D-files can be downloaded at <a href="https://www.printables.com/de/model/459099-gusi-radio">printables.com</a>


<hr>

<h3 style='color: #16A085; font-size: 2em;'><img src="images/icon_software.svg" alt=(DE) style="height:22px"> Software installation</h3>


<h3>1) Install the OS</h3>

 Install Raspberry Pi OS lite on the SD card. You can use the tool <a href="https://www.raspberrypi.org/software/">Raspberry Pi imager</a>

<b>Raspberry Pi device:</b><br>
Raspberry Pi zero / Raspberry Pi zero 2


<b>Operating system:</b><br> 
Raspberry Pi OS Bullseye (64-Bit)

<div class="warning" style='padding:0.8em; background-color:#F1C40F; color:black'>
Make sure you select "Bullseye" and not "Bookworm" for the Debian version, <br>as the OnOFF SHIM and start.py will not run under Bookworm!
</div><br>

<b>Storage:</b><br> 
elect the SD-Card

Klick on the <b>Next</b> button and allow OS customisation.

<b>General</b>
<li>Hostname: Gusi
<li>Username: gusi
<li>Password: your choise
<li>Set up WIFI: Enter the WiFi login data here
<li>Select your WiFI country
<li>Select time location an keyboard layout
</ul><br><br>

<b>Services</b><br> 
Enable <b>SSH</b> (password)<br><br>

<hr>

<h3>2) SSH Connection</h3>


<color style='color: #16A085'>2.1)</color> Insert the card into the Raspberry and let it boot up. Find out which IP address your Pi got. (You can try ```ping gusi``` in terminal).


<color style='color: #16A085'>2.2)</color> Access the Raspberry via SSH:
```ssh gusi@192.168.1.100```

<hr>

<h3>3) Install the Software</h3> 

<color style='color: #16A085'>3.1)</color> Prepare the configuration file:<br>
  ```
  sudo nano /boot/config.txt
  ```

Comment out the line ```dtparam=audio=off``` by inserting a ‘#’ in front of it. It should look like this: 
```#dtparam=audio=off``` 

Insert the following code at the end of the file:<br>
```
################## GUSI ################
# Disable Bluetooth
dtoverlay=pi3-disable-bt

# Enable Hifiberry Soundcard
dtoverlay=hifiberry-dac
```

Save the change with ```CTRL``` + ```X``` and confirm with ```Y``` and ```Enter```



<br><color style='color: #16A085'>3.2)</color> Install the required packages <br>
```
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install -y git mpd mpc alsa-utils python3-pip python3-gpiozero
```

<br><color style='color: #16A085'>3.3)</color> Install the required packages <br>
```
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install -y git mpd mpc alsa-utils python3-pip python3-gpiozero
```
<br><color style='color: #16A085'>3.4)</color> Install the OnOff SHIM for the power control <br>
```
curl https://get.pimoroni.com/onoffshim | bash
``` 
Let the device restart

<br><color style='color: #16A085'>3.5)</color> Clone the Git repository <br>
```
git clone https://github.com/earlmckay/gusi-radio.git
```

<br><color style='color: #16A085'>3.6)</color> Make the script executable and run it (choose between German and English):<br>
<img src="images/flag_de.svg" alt=(DE) style="width:16px"> For German:
```
chmod +x /home/gusi/gusi-radio/setup_gusi_DE.sh
```
```
sudo /home/gusi/gusi-radio/setup_gusi_DE.sh
```
<br>

<img src="images/flag_en.svg" alt=(EN) style="width:16px"> For English:
```
chmod +x /home/gusi/gusi-radio/setup_gusi_DE.sh
```
```
sudo /home/gusi/gusi-radio/setup_gusi_DE.sh
```

<hr>

<h3>4) Customize the Software</h3> 

<color style='color: #16A085'>4.1)</color> Customise the radio stations in the gusi.py:<br>


```
sudo nano /home/gusi/gusi-radio/gusi.py
```

Each time the button is pressed, the script switches to the next station (defined in variables S1, S2, S3), and an announcement (s1.mp3, s2.mp3, s3.mp3) is played to indicate which station can now be heard.) The announcements are generic and say “Station one”. 

<b>Customize radio station:</b><br>
Change the URLs for "S1", "S2" and "S3" in the "VAR DEFINITIONS" area.

<div class="warning" style='padding:0.8em; background-color:#999999; color:black'>
#---------- VAR DEFINITION ----------#<br>
S1 = "https://server7.stream.com/stream"<br>
S2 = "http://www.sw.de:8000/de"<br>
S3 = "https://streamplus.de/stream.mp3"<br>
</div><br>

If more stations are needed, the list of variables can be extended with "S4", "S5" ... .<br>

<b>Set order:</b><br>
By listing the channels defined above, you can choose which should be included in the rotation and in which order.
<div class="warning" style='padding:0.8em; background-color:#999999; color:black'>
#---------- RADIO STATIONS ORDER ----------#<br>
stations = [S1, S2, S3]<br>
</div><br>

<b>Alignment of the announcements:</b><br>
Sort the order of the announcements according to the order of the stations (S1 = s1.mp3). <br>
Also make sure that the number of stations and announcements is the same! 
<div class="warning" style='padding:0.8em; background-color:#999999; color:black'>
#---------- ANNOUNCEMENTS ORDER ----------#<br>
announcements = ["s1.mp3", "s2.mp3", "s3.mp3"]
</div><br>
<b>Customized announcements:</b><br>
You can, of course, generate your own announcements (by recording them yourself or using TTS). For better identification, the name of the station can be played, for example.<br><br>

You can place the newly generated announcements under the following path: 
```/var/lib/mpd/music/```
<br>(This folder also contains all other radio announcements (e.g. error announcements). You can also regenerate and replace these if necessary.)

As soon as there is a change in the music folder, you must update the database:
```
mpc update
```


<br>

<color style='color: #16A085'>4.2)</color> Customise the WiFi Country in the auto-wps.py:<br>

```
nano /home/gusi/gusi-radio/auto_wps.py
```

Search for "country" (Linie 35):


<div class="warning" style='padding:0.8em; background-color:#999999; color:black'>
print("reset wpa_supplicant.conf")<br>
new_config = """ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev<br>
update_config=1<br>
country=<b>DE</b><br>
</div><br>

Replace DE with the required country code (for example "GB")

<hr>

<h3 style='color: #16A085; font-size: 2em;'><img src="images/icon_assembly.svg" alt=(DE) style="height:22px"> Hardware installation</h3>

<h3>5.1) Prepare Cable</h3>
Following cable lengths are required:
<ul>
<li> Loudspeaker: 2 x 120 mm
<li> Rotary encoder: 5 x 200 mm
<li> Pushbutton: 2 x 200 mm
<li> OnOff SHIM: 2 x 100 mm
<li> LED: 2 x 160 mm
</ul>


Insulate both ends by approx. 3 mm.

<hr>

<h3>5.2) Rotary encoder</h3>
The Rotary Encoder has a total of 5 pins:

<ul>
<li>  GRD: Ground
<li>  +: voltage
<li>  SW: Push
<li>  CLK: Primary rotation
<li>  DT: Phase shifted rotation 
</ul>

Crimp the 5 prepared cables with a female Dupon connector on each side and connect the cables to the Rotary Encoder.

![](images/install_rotary_encoder_cable.jpg)

<h3>5.3) Prepare the pushbutton</h3>
For the pushbutton, one part of the cables must be soldered to the button, the other ends get a female Dupon connector.
Crimp the 5 prepared cables with a female Dupon connector on each side and connect the cables to the Rotary Encoder.

![](images/install_button_cable.jpg)

<h3>5.4) Insert the rotary control and the button</h3>
Now you can screw the rotary encoder into the middle hole of the case. Make sure that it sits straight, otherwise the knob will wobble.
The push button is inserted into the outside of the case. It should snap into place. 

![](images/install_buttons.jpg)


<h3>5.5) Power supply</h3>

Before you insert the power socket, solder the cables first. This is more comfortable and avoids damaging the plastic housing. 
Seen from the back, the positive pole is on the left and the negative pole on top.

Now you can solder the cables to the micro USB connector. 
The left contact is the positive pole, the one on the right side is the negative pole (see picture).

![](images/install_power_cable.jpg)
![](images/install_power_input.jpg)

------------

 <h3>5.6) Loudspeaker</h3>

First the easy part. Solder two cables to the two speaker contacts. 
The other ends of the cables do not need to be worked on, as they will be clamped into the amplifier later. 

Before you screw in the speaker, the speaker grille must be inserted first. Make sure that the holes are exactly aligned with those in the housing.
Now place the speaker in the cabinet on the grille and fix it with the 6 mm screws.

![](images/install_speaker.jpg)

------------

 <h3>5.7) LED</h3>
For the LED you need the two prepared cables and two female Dupon connectors, which are crimped on one side of the cable. 
The other sides have to be soldered to the LED itself. I used here for the anode (longer pin of the LED) the red cable and for the shorter side (cathode) the black cable. To avoid a short circuit, a heat shrink tube can be used.
Now push the LED into the holder.

![](images/install_led_cable.jpg)

------------

 <h3>5.8) OnOff SHIM</h3>
The board comes with optional female connectors, which I also used. For the two button contacts I cut and soldered two male Dupon connectors.
The pre-assembled cables can now be equipped with a male Dupon connector on one end and a female connector on the other end. 

![](images/install_shim_onoff_cable.jpg)

<hr>

 <h3>5.9) Connection</h3>
First, the Raspberry can be screwed to the lower base plate.
Then the GPIO corner adapter can be plugged on, followed by the MiniAmp.

Then everything can be connected one by one.

1) Rotary Encoder to Raspberry
2) SHIM OnOff with Raspberry
3) Pushbutton with SHIM OnOff
4) LED with Raspberry
5) Power supply with SHIM On Off
6) Speaker with MiniAmp

![](images/gpio_sheet.png)
![](images/GuSi_fzz.png)
![](images/install_components_together.jpg)

<hr>

Finally, I would like to thank [Robert Nickel](https://github.com/Robert-Nickel) for his support, as well to [Notification Sounds](https://notificationsounds.com/) for providing the sounds.


<style>
h1 {
  color: #16A085;
  font-size: 6em;
  border-bottom: 0;
}

h2 {
  color: #16A085;
  font-size: 2em;
  border-bottom: 0;
}

h3 {
  color: #16A085;
}

/* unvisited link */
a:link {
  color: #16A085;
}

/* visited link */
a:visited {
  color: #16A085;
}

/* mouse over link */
a:hover {
  color: #16A085;
}

/* selected link */
a:active {
  color: #16A085;
}
</style>