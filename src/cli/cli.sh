#!/bin/bash
function facerec(){
if [ "$1" = "new" ]; then
    sudo python3 /lib/Auth/Facerec/add_new.py
elif [ "$1" = "enable" ]; then
    sudo cp /lib/Auth/Facerec/Facerec /usr/share/pam-configs/
    sudo cp /lib/Auth/Facerec/facerec /usr/share/bash-completion/completions/
    sudo pam-auth-update --package
elif [ "$1" = "disable" ]; then
    sudo rm /usr/share/pam-configs/Facerec
    sudo rm /usr/share/bash-completion/completions/facerec
    sudo python3 /lib/Auth/Facerec/remove_cli.py
    sudo pam-auth-update --package
elif [ "$1" = "remove" ]; then
    sudo python3 /lib/Auth/Facerec/remove_cli.py
    sudo chattr -R -i /lib/Auth/
    sudo rm -r /lib/Auth
    sudo rm /usr/share/pam-configs/Facerec
    sudo rm /usr/share/bash-completion/completions/facerec
    sudo pam-auth-update --package
fi
}
