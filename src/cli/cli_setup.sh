#!/bin/bash
echo 'source /lib/Auth/Facerec/cli.sh' >> ~/.bashrc
echo 'QT_X11_NO_MITSHM=1' >> /etc/environment
. ~/.bashrc
