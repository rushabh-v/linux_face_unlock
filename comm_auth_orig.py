
if __name__ == '__main__':
    f = open("/etc/pam.d/polkit-1", "r")
    text = f.read()
    if "common-auth-orig" not in text and "common-auth" in text:
        text = text.replace("common-auth", "common-auth-orig")
        f = open("/etc/pam.d/polkit-1", "w+")
        f.write(text)
    f.close()

    f = open("/etc/default/apport", "r")
    text = f.read()
    if "enabled=1" in text:
        text = text.replace("enabled=1", "enabled=0")
        f = open("/etc/default/apport", "w+")
        f.write(text)
    f.close()
