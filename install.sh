#!/bin/bash
mkdir /lib/Auth
mkdir /lib/Auth/Facerec
mkdir /lib/Auth/Facerec/roots
cp -a ./src/utils/. /lib/Auth/Facerec/
cp -a ./src/cli/. /lib/Auth/Facerec/
cp -a ./src/keyring/. /lib/Auth/Facerec/
cp -a ./* /lib/Auth/Facerec/
sudo cp ./src/cli/facerec /usr/share/bash-completion/completions/
cp pam_python.so /lib/x86_64-linux-gnu/security/
cd /lib/Auth/Facerec/
chmod +x cli.sh cli_setup.sh
chmod -w cli_setup.sh cli.sh getFaces.py add_new.py compare.py pam_ptn.py comm_auth_orig.py remove_cli.py  keyring_disable.py keyring_enable.py facerec Facerec roots
chattr +i cli_setup.sh cli.sh getFaces.py add_new.py compare.py pam_ptn.py comm_auth_orig.py remove_cli.py  keyring_disable.py keyring_enable.py facerec Facerec roots
./cli_setup.sh
. ~/.bashrc
