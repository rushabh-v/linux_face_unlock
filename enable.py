from os import system
print("Enter 'y' id you want to add your face now else press 'n':")
s = input()
if s=='y':
    system("python ./add_new.py")
    print("Enter 'y' id you want to enable the face unlock now else press 'n'")
    s = input()
    if s=='y':
        system("sudo pam-auth-update --package")
    else:
        pass
else:
    pass




