from os import system

if __name__ == '__main__':
    system("sudo chmod +x install.sh")
    system("sudo chmod +x requirements.sh")
    system("./requirements.sh")
    system("sudo -H ./requirements.sh")
    system("sudo ./install.sh")
    system("sudo python ./comm_auth_orig.py")
    print("run 'facerec new' to add new face and\n'facerec enable' to enable the facerec.")
