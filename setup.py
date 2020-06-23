from os import system

if __name__ == '__main__':
    system("sudo chmod +x install.sh")
    system("sudo chmod +x requirements.sh")
    system("./requirements.sh")
    system("sudo -H ./requirements.sh")
    system("sudo ./install.sh")
    print("run 'facerec new' to add new face and\n'facerec enable' to enable the facerec.")
    f = open("/etc/pam.d/polkit-1", "r")
    text = f.read()
    if "common-auth" in text:
        text.replace("common-auth", "common-auth-orig")
    