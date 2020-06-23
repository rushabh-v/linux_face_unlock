#!/bin/bash
mkdir /lib/Auth
mkdir /lib/Auth/RecFace
mkdir /lib/Auth/RecFace/roots
cp -a ./. /lib/Auth/RecFace/
cp /etc/pam.d/common-auth /etc/pam.d/common-auth-orig
cp Recface /usr/share/pam-configs/
cp pam_python.so /lib/x86_64-linux-gnu/security/
cd /lib/Auth/RecFace/
chmod +x addcmd.sh recface.sh
chmod -w addcmd.sh recface.sh getFaces.py enable.py install.sh add_new.py compare.py pam_ptn.py Recface roots
chattr +i addcmd.sh recface.sh getFaces.py enable.py install.sh add_new.py compare.py pam_ptn.py Recface roots
./addcmd.sh
. ~/.bashrc
