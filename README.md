
# Linux Face Unlock

A blog on How I built this project can be found [here](https://medium.com/analytics-vidhya/how-i-built-face-unlock-for-ubuntu-linux-a2b769d1fbc1).

I am working on creating a PPA. It will be available shortly.

## Installation: (Temporary)

1. Install prerequisites:

```
sudo apt-get install python3-pip \
    python3-opencv \
    python3-setuptools \
    python-execnet \
    cmake \
    libatlas-base-dev \
    build-essential
```

2. Download the deb package:

```
wget https://rushabh-v.github.io/facerec_2.0_all.deb
```

3. Install facerec:

```
dpkg -i facerec_2.0_all.deb
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

