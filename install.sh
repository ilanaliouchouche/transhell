#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run with administrator privileges." 
   exit 1
fi

cp trans /usr/local/bin/
cp model_trans.py /usr/local/bin/

chmod +x /usr/local/bin/trans

prompt_install() {
    local prompt=$1
    local install_cmd=$2

    while true; do
        read -p "$prompt [y/n]: " yn
        case $yn in
            [Yy]* ) eval $install_cmd; break;;
            [Nn]* ) exit 1;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    prompt_install "Python is required, but it's not installed. Would you like to install it now?" "sudo apt-get install python3"
fi

if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    prompt_install "pip is required, but it's not installed. Would you like to install it now?" "sudo apt-get install python3-pip"
fi

if [[ -f requirements.txt ]]; then
    pip install -r requirements.txt
else
    echo "No requirements.txt file found. Skipping dependency installation."
fi

echo "Installation completed. You can now use the 'trans' command in your terminal."

