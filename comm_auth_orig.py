
if __name__ == '__main__':
    f = open("/etc/pam.d/polkit-1", "r")
    text = f.read()
    if "common-auth-orig" not in text and "common-auth" in text:
        text = text.replace("common-auth", "common-auth-orig")
        f = open("/etc/pam.d/polkit-1", "w+")
        f.write(text)
    f.close()
