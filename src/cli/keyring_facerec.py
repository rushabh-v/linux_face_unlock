
if __name__ == '__main__':
    f = open("/usr/share/pam-configs/gnome-keyring", "r")
    text = f.read()
    if "pam_ptn" not in text:
        ind = text.index("optional") - 1
        text = (text[:ind]
                + "    optional    pam_python.so /lib/Auth/Facerec/pam_ptn.py\n"
                + text[ind:]
        )
        f = open("/usr/share/pam-configs/gnome-keyring", "w+")
        f.write(text)
        f.close()
    else:
        f.close()
