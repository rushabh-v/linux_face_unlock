if __name__ == '__main__':
    f = open("/etc/pam.d/polkit-1", "r")
    text = f.read()
    if "common-auth" in text:
        text = text.replace("common-auth", "common-auth-orig")
        f = open("/etc/pam.d/polkit-1", "w+")
        f.write(text)
        f.close()
    else:
        raise Exception('"common-auth" not found in /etc/pam.d/polkit-1')
