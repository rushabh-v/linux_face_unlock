
# Linux Face Unlock

A blog on How I built this project can be found [here](https://medium.com/analytics-vidhya/how-i-built-face-unlock-for-ubuntu-linux-a2b769d1fbc1).

### Installation steps:
1. Clone the repository:

```
git clone https://github.com/rushabh-v/linux_face_unlock.git
cd linux_face_unlock
```

2. Make the `install.sh` file executable:

```
chmod +x install.sh
```

3. Run the `install.sh` script:

```
sudo ./install.sh
```

4. Add a new root face:

```
facerec new
```
     
5. Enable the facerec:

```
facerec enable
```

## Troubleshoot

* If you don't have root access. Go to recovery mode as root and run,

```
apt-get --reinstall install libpam-runtime libpam-modules
```




