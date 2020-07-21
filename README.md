
# Linux Face Unlock

A blog on How I built this project can be found [here](https://medium.com/analytics-vidhya/how-i-built-face-unlock-for-ubuntu-linux-a2b769d1fbc1).
The debian package is currently being worked on! Follow the steps to install master.
## Installation:
1. Clone the repository:

```
git clone https://github.com/rushabh-v/linux_face_unlock.git
cd linux_face_unlock
```


2. Run the `setup.py` script:

```
python3 setup.py
```
## Command Line Interface

| Command | Discription |
|---------|:------------|
| facerec new | Add a new root face.|
| facerec enable | Enable facerec back.|
| facerec disable | Temporarily disable facerec, preserving the setup. |
| facerec remove | Completely remove the facerec and the root faces.  |
| facerec --help | Get info about the facere CLI |



## Troubleshoot

* If you don't have root access. Go to recovery mode as root and run,

```
facerec remove
```




