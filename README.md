# Facerec 

# Installation:
step 1: clone the repo using

$ git clone https://github.com/RushabhVasani/linux_face_unlock.git

step 2: Go to the cloned directory using cd.

(Generally at home/USER/Linux_face_unlock ("cd Linux_face_unlock" in this case))

step 3: make the install.sh file executable by:

$ chmod +x install.sh

step 4: Run the install.sh script using:

$ sudo ./install.sh

step 5: run "facerec new" if you want to add a new root face.

$ facerec new

step 6: run "facerec enable" to enable the facerec.

$ facerec enable

By chance if due to any error it is not allowing you to go root,

Go to recovery mode as root and run,

$ apt-get --reinstall install libpam-runtime libpam-modules
