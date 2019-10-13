#!/bin/bash
apt update
apt-get install unzip
apt install python-pip
apt install python3-pip
pip install opencv-python
pip install fastai
unzip Images.zip
mv Images images
mkdir /lib/Auth
mkdir /lib/Auth/RecFace
cp -a ./. /lib/Auth/RecFace/
cp Recface /usr/share/pam-configs/
cp pam_python.so /lib/x86_64-linux-gnu/security/
cd /lib/Auth/RecFace/
chmod +x addcmd.sh
chmod +x recface.sh
./addcmd.sh
python ./enable.py




