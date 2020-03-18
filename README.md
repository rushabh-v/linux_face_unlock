
# Facerec

A blog on How I built this project can be found [here](https://medium.com/analytics-vidhya/how-i-built-face-unlock-for-ubuntu-linux-a2b769d1fbc1).

### Installation steps:
1. clone the repo.

     * `git clone https://github.com/rushabh-v/linux_face_unlock.git`

1. Go to the cloned directory using cd.(Generally at home/USER/Linux_face_unlock)

     * `cd Linux_face_unlock`

1. make the install.sh file executable by:

     * `chmod +x install.sh`

1. Run the install.sh script using:

      * `sudo ./install.sh`

1. run "facerec new" if you want to add a new root face.

     * `facerec new`
     
 1. run "facerec enable" to enable the facerec.

     * `facerec enable`

#### By chance due to any error if it is not allowing you to go root then don't panic just Go to recovery mode as root and run,

  * `apt-get --reinstall install libpam-runtime libpam-modules`




