#!/bin/bash

echo "Stop MPD service"
sudo service mpd stop

echo "Moving files"
sudo mv /home/gusi/gusi-radio/8192cu.conf /etc/modprobe.d/
sudo mv /home/gusi/gusi-radio/asound.conf /etc/
sudo mv /home/gusi/gusi-radio/mpd.conf /etc/
sudo mv /home/gusi/gusi-radio/EN/* /var/lib/mpd/music/
sudo mv /home/gusi/gusi-radio/cleanshutd.conf /etc/
sudo mv /home/gusi/gusi-radio/rc.local /etc/

echo "Cleaning up"
sudo rm -r /home/gusi/gusi-radio/DE
sudo rm -r /home/gusi/gusi-radio/EN
sudo rm -r /home/gusi/gusi-radio/.gitattributes
sudo rm -r /home/gusi/gusi-radio/.gitignore
sudo rm -r /home/gusi/gusi-radio/LICENSE
sudo rm -r /home/gusi/gusi-radio/README.md
sudo rm -r /home/gusi/gusi-radio/.git
sudo rm -r /home/gusi/gusi-radio/onoffshim
sudo systemctl stop dphys-swapfile
sudo systemctl disable dphys-swapfile
sudo systemctl disable keyboard-setup.service
sudo systemctl disable triggerhappy.service
sudo /usr/bin/tvservice -o

echo "Set permission"
sudo chmod +x /etc/rc.local
sudo chmod -R g+w /var/lib/mpd
sudo chmod -R g+w /var/run/mpd

echo "Start MPD service"
sudo systemctl enable mpd.service
sudo service mpd start

echo "Refresh MPD"
mpc update

echo "Installation finished. The device will reboot now."

sudo reboot 