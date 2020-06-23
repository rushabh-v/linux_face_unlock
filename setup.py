from os import listdir, system
from os.path import isfile, join

if __name__ == '__main__':
    system("sudo chmod +x install.sh")
    system("sudo chmod +x requirements.sh")
    system("./requirements.sh")
    system("sudo -H ./requirements.sh")
    system("sudo ./install.sh")
    path = "/etc/pam.d/"
    pamd = [f for f in listdir(path) if isfile(join(path, f))]
    if "common-auth-orig" not in pamd:
        system("cp /etc/pam.d/common-auth /etc/pam.d/common-auth-orig")
        system("sudo python ./comm_auth_orig.py")
    print("run 'facerec new' to add new face and\n'facerec enable' to enable the facerec.")
