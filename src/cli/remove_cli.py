from os.path import expanduser

if __name__ == '__main__':

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
