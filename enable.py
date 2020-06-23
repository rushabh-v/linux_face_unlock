from os import system

if __name__ == '__main__':
    print("Enter 'y' id you want to add your face now else press 'n':")
    s = input()
    if s=='y':
        system("sudo python3 ./add_new.py")
        print("Enter 'y' id you want to enable the face unlock now else press 'n'")
        s = input()
        if s=='y':
            system("sudo pam-auth-update --package")
        else:
            pass
    else:
        pass
