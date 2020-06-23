#!/bin/bash
function facerec(){
if [ "$1" = "new" ]; then
    sudo python3 /lib/Auth/RecFace/add_new.py
elif [ "$1" = "enable" ]; then
    sudo cp /lib/Auth/RecFace/RecFace /usr/share/pam-configs/
    sudo pam-auth-update --package
elif [ "$1" = "disable" ]; then
    sudo rm /usr/share/pam-configs/Recface
    sudo pam-auth-update --package
fi
}
