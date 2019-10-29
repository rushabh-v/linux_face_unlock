#!/bin/bash
apt-get install unzip
apt install python-pip
apt install python3-pip
sudo -H pip3 install execnet
sudo -H pip install execnet
sudo -H pip3 install opencv-python
sudo -H pip3 install --no-cache-dir -U --timeout 20000 fastai
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
echo "run 'facerec new' to add new face and 'facerec enable' to enable the facerec."
