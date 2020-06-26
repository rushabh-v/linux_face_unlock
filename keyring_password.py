
if __name__ == '__main__':
    f = open("/usr/share/pam-configs/gnome-keyring", "r")
    text = f.read()
    l = "    optional    pam_python.so /lib/Auth/Facerec/pam_ptn.py\n"
    if l in text:
        ind = text.index(l)
        text = text[:ind] + text[ind+len(l):]
        f = open("/usr/share/pam-configs/gnome-keyring", "w+")
        f.write(text)
    f.close()
