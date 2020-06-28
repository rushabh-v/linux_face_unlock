from os.path import expanduser

if __name__ == '__main__':
    
    # Fix /usr/share/pam-configs/gnome-keyring
    f = open("/usr/share/pam-configs/gnome-keyring", "r")
    text = f.read()
    l = "    optional    pam_python.so /lib/Auth/Facerec/pam_ptn.py\n"
    if l in text:
        ind = text.index(l)
        text = text[:ind] + text[ind+len(l):]
        f = open("/usr/share/pam-configs/gnome-keyring", "w+")
        f.write(text)
    f.close()

    # Fix ~/.bashrc
    bashrc = expanduser("~") + "/.bashrc"
    f = open(bashrc, "r")
    text = f.read()
    f.close()
    if "source /lib/Auth/Facerec/cli.sh" in text:
        text = text.replace("source /lib/Auth/Facerec/cli.sh", "")
        f = open(bashrc, "w+")
        f.write(text)
        f.close()
