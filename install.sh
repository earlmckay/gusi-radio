#!/bin/bash

echo "GuSi installer"

sudo apt-get update && sudo apt-get upgrade -y
echo "1) System updated"

sudo apt-get install mpd alsa-utils -y
echo "2) Music Player Daemon installed"

sudo apt-get install git -y
echo "3) Git installed"

sudo apt-get install python3-pip -y
echo "4) Python3-pip installed"

sudo apt-get install python3-gpiozero -y
echo "5) gpiozero installed"

git clone https://github.com/earlmckay/gusi-radio
echo "6) GuSi Repository cloned"

sudo mv /home/gusi/gusi-radio/rc.local /etc/
sudo chmod a+x /etc/rc.local
echo "8) Autostart installed"

sudo mv /home/gusi/gusi-radio/cleanshutd.conf nach /etc/ 
echo "9) Cleanshutdown replaced"

echo -e "options 8192cu rtw_power_mgnt=0 rtw_enusbss=0\nrtw_ips_mode=1" | sudo tee /etc/modprobe.d/8192cu.conf
echo "12) 8192cu.conf updated"

echo -e "\n\n################## GUSI ################\n# Disable Bluetooth\ndtoverlay=pi3-disable-bt\n\n# Enable Hifiberry Soundcard\ndtoverlay=hifiberry-dac" | sudo tee -a /boot/config.txt
echo "13) Enabled HiFi Berry in config.txt"

echo -e "pcm.hifiberryMiniAmp {\n    type softvol\n    slave.pcm \"plughw:0\"\n    control.name \"Master\"\n    control.card 0\n}\npcm.!default {\n    type       plug\n    slave.pcm  \"hifiberryMiniAmp\"\n}" | sudo tee -a /etc/asound.conf
echo "14) Set HiFi Berry as main sound card"

sudo service dphys-swapfile stop
echo "15) dphys-swapfile stopped"

sudo systemctl disable dphys-swapfile
echo "16) dphys-swapfile disabled"

sudo systemctl disable keyboard-setup.service
echo "17) keyboard-setup.service disabled"

sudo systemctl disable triggerhappy.service
echo "18) triggerhappy.service disabled"

sudo /usr/bin/tvservice -o
echo "19) Screen turned off"

read -p "Enter WLAN region code (e.g., DE or EN): " wlan_region
sudo raspi-config nonint do_wifi_country $wlan_region

read -p "Select language (EN or DE): " selected_language

if [ "$selected_language" == "EN" ]; then
    sudo mv /home/gusi/gusi-radio/EN/mpd.conf /etc/
    rm -r /home/gusi/gusi-radio/announcements/DE
elif [ "$selected_language" == "DE" ]; then
    sudo mv /home/gusi/gusi-radio/DE/mpd.conf /etc/
    rm -r /home/gusi/gusi-radio/announcements/EN
else
    echo "Invalid language selection."
fi

mpc update
echo "20) Updated music database"

chmod a+x home/gusi/gusi-radio/onoffshim.sh
bash /home/gusi/gusi-radio/onoffshim.sh
echo "ShimOnOFF installed"

echo "GuSi successfully installed!"
