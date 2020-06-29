
# Linux Face Unlock

A blog on How I built this project can be found [here](https://medium.com/analytics-vidhya/how-i-built-face-unlock-for-ubuntu-linux-a2b769d1fbc1).

### Installation steps:
1. Clone the repository:

```
git clone https://github.com/rushabh-v/linux_face_unlock.git
cd linux_face_unlock
```


2. Run the `setup.py` script:

```
python3 setup.py
```

3. Add a new root face:

```
facerec new
```
     
4. Enable the facerec:

```
facerec enable
```

5. Temporarily disable facerec:
```
facerec disable
```

6. Completely remove the facerec and the root faces:
```
facerec remove
```

## Troubleshoot

* If you don't have root access. Go to recovery mode as root and run,

```
facerec remove
```




