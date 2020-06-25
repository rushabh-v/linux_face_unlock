#!/bin/bash
mkdir /lib/Auth
mkdir /lib/Auth/Facerec
mkdir /lib/Auth/Facerec/roots
cp -a ./utils/. /lib/Auth/Facerec/
cp -a ./cli/. /lib/Auth/Facerec/
cp pam_python.so /lib/x86_64-linux-gnu/security/
cd /lib/Auth/Facerec/
chmod +x cli.sh cli_setup.sh
chmod -w addcmd.sh recface.sh getFaces.py enable.py install.sh add_new.py compare.py pam_ptn.py Recface roots
chattr +i addcmd.sh recface.sh getFaces.py enable.py install.sh add_new.py compare.py pam_ptn.py Recface roots
./cli_setup.sh
. ~/.bashrc
