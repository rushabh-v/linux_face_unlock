#!/bin/bash
mkdir /lib/Auth
mkdir /lib/Auth/Facerec
mkdir /lib/Auth/Facerec/roots
cp -a ./src/utils/. /lib/Auth/Facerec/
cp -a ./src/cli/. /lib/Auth/Facerec/
cp -a ./* /lib/Auth/Facerec/
cp pam_python.so /lib/x86_64-linux-gnu/security/
cd /lib/Auth/Facerec/
chmod +x cli.sh cli_setup.sh
chmod -w cli_setup.sh cli.sh getFaces.py add_new.py compare.py pam_ptn.py roots comm_auth_orig.py keyring_password.py keyring_facerec.py
chattr +i cli_setup.sh cli.sh getFaces.py add_new.py compare.py pam_ptn.py roots comm_auth_orig.py keyring_password.py keyring_facerec.py
./cli_setup.sh
. ~/.bashrc
exec bash
