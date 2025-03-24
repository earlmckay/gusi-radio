#!/bin/bash

LANGUAGE=""
LANGUAGE_CODE=""
MODEL=""
MODEL_CODE=""

# Function for language selection
select_language() {
    echo "Please select the language for the radio:"
    echo "1) DE"
    echo "2) EN"
    echo "3) RU"
    
    while true; do
        read -p "Please enter your choice (1-3): " lang_choice
        
        case $lang_choice in
            1)
                LANGUAGE="German"
                LANGUAGE_CODE="DE"
                break
                ;;
            2)
                LANGUAGE="English"
                LANGUAGE_CODE="EN"
                break
                ;;
            3)
                LANGUAGE="Russian"
                LANGUAGE_CODE="RU"
                break
                ;;
            *)
                echo "Invalid choice. Please select 1, 2, or 3."
                ;;
        esac
    done
    
    echo "Selected language: $LANGUAGE ($LANGUAGE_CODE)"
    echo ""
}

# Function for model selection
select_model() {
    echo "Please select radio model:"
    echo "1) BM1K"
    echo "2) BM2K"
    echo "3) RM5K"
    
    while true; do
        read -p "Please enter your choice (1-3): " model_choice
        
        case $model_choice in
            1)
                MODEL="GUSI-Radio with power button"
                MODEL_CODE="BM1K"
                break
                ;;
            2)
                MODEL="GUSI-Radio with power and play/pause button"
                MODEL_CODE="BM2K"
                break
                ;;
            3)
                MODEL="GUSI-Radio Retro with five buttons"
                MODEL_CODE="RM5K"
                break
                ;;
            *)
                echo "Invalid choice. Please select 1, 2, or 3."
                ;;
        esac
    done
    
    echo "Selected model: $MODEL ($MODEL_CODE)"
    echo ""
}

# Main function for installation
install() {
    echo "Starting installation process..."
    echo "Language: $LANGUAGE ($LANGUAGE_CODE)"
    echo "Model: $MODEL ($MODEL_CODE)"
    
    # Specific configuration depending on model
    if [ "$MODEL_CODE" = "BM1K" ]; then
        echo "Configuring BM1K"
        sudo mv /home/gusi/gusi-radio/setup_files/gusi_BM.py /home/gusi/gusi-radio/gusi.py

    elif [ "$MODEL_CODE" = "BM2K" ]; then
        echo "Configuring BM2K"
        sudo mv /home/gusi/gusi-radio/setup_files/gusi_BM.py /home/gusi/gusi-radio/gusi.py

    elif [ "$MODEL_CODE" = "RM5K" ]; then
        echo "Configuring RM5K"
        sudo mv /home/gusi/gusi-radio/setup_files/gusi_RM.py /home/gusi/gusi-radio/gusi.py
    fi


    # Common commands for all models
    echo "Stop MPD service"
    sudo service mpd stop
    
    sudo mv /home/gusi/gusi-radio/setup_files/8192cu.conf /etc/modprobe.d/
    sudo mv /home/gusi/gusi-radio/setup_files/asound.conf /etc/
    sudo mv /home/gusi/gusi-radio/setup_files/mpd.conf /etc/
    sudo mv /home/gusi/gusi-radio/setup_files/cleanshutd.conf /etc/
    sudo mv /home/gusi/gusi-radio/setup_files/rc.local /etc/
    sudo mv "/home/gusi/gusi-radio/setup_files/$LANGUAGE_CODE/wifi_fallback.html" /home/gusi/gusi-radio/wifi-setup/
    sudo mv "/home/gusi/gusi-radio/setup_files/$LANGUAGE_CODE/wifi_fallback.py" /home/gusi/gusi-radio/wifi-setup/
    sudo mv "/home/gusi/gusi-radio/setup_files/$LANGUAGE_CODE/"* /var/lib/mpd/music/
    
    echo "Process optimization"
    sudo systemctl stop dphys-swapfile
    sudo systemctl disable dphys-swapfile
    sudo systemctl disable keyboard-setup.service
    sudo systemctl disable triggerhappy.service
    sudo /usr/bin/tvservice -o
    
    echo "Set permission"
    sudo chmod +x /etc/rc.local
    sudo chmod -R g+w /var/lib/mpd
    sudo chmod -R g+w /var/run/mpd
    sudo chmod +x /home/gusi/gusi-radio/wifi-setup/wifi_fallback.py
    sudo chmod 644 /home/gusi/gusi-radio/wifi-setup/wifi_fallback.html
    sudo chmod +x /home/gusi/gusi-radio/wifi-setup/auto-wps.py
    sudo chmod +x /home/gusi/gusi-radio/gusi.py
    sudo chmod +x /home/gusi/gusi-radio/start.py

    echo "Stopping services for hotspot setup"
    sudo systemctl unmask hostapd
    sudo systemctl stop hostapd
    sudo systemctl stop dnsmasq

    echo "Disabling services for hotspot setup"
    sudo systemctl disable hostapd
    sudo systemctl disable dnsmasq

    echo "Start MPD service"
    sudo systemctl enable mpd.service
    sudo service mpd start

    echo "Refresh MPD"
    mpc update


    echo "Installation completed successfully!"
    echo "Next, please install the OnOffSHIM with the command \"curl https://get.pimoroni.com/onoffshim | bash\"."
    
    echo "Cleaning up installation files..."
    sudo rm -r /home/gusi/gusi-radio/images 2>/dev/null
    sudo rm -r /home/gusi/gusi-radio/.gitattributes 2>/dev/null
    sudo rm -r /home/gusi/gusi-radio/.gitignore 2>/dev/null
    sudo rm -r /home/gusi/gusi-radio/LICENSE 2>/dev/null
    sudo rm -r /home/gusi/gusi-radio/.git 2>/dev/null
    sudo rm -r /home/gusi/gusi-radio/README.md 2>/dev/null

    (sleep 2 && sudo rm -rf /home/gusi/gusi-radio/setup_files) &

# Main
echo "GuSi installation script"
echo "========================="
echo ""

# Perform user queries
select_language
select_model

# Confirmation before installation
echo "Ready to install with the following configuration:"
echo "Language: $LANGUAGE ($LANGUAGE_CODE)"
echo "Model: $MODEL ($MODEL_CODE)"
read -p "Continue with installation? (y/n): " confirm

if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    install
else
    echo "Installation cancelled."
    exit 0
fi