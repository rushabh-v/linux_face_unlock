from os import listdir, system
from os.path import isfile, join

if __name__ == '__main__':
    system("sudo apt-get install python-pip")
    system("sudo apt-get install python3-pip")
    system("sudo apt-get install libatlas-base-dev")
    system("sudo apt - get install build-essential")
    system("sudo chmod +x requirements.sh")
    system("./requirements.sh")
    system("sudo -H ./requirements.sh")
    system("sudo chmod +x install.sh")
    system("sudo ./install.sh")
    path = "/etc/pam.d/"
    pamd = [f for f in listdir(path) if isfile(join(path, f))]
    if "common-auth-orig" not in pamd:
        system("sudo cp /etc/pam.d/common-auth /etc/pam.d/common-auth-orig")
    system("sudo python3 ./comm_auth_orig.py")
    print("run 'facerec new' to add new face and\n'facerec enable' to enable the facerec.")
