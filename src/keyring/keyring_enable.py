from os import listdir, system
from os.path import isfile, join

if __name__ == '__main__':

    path = "/etc/pam.d/"
    gk = "gnome_keyring.so"
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    for file_path in files:
        flag = False
        f = open(file_path, "r")
        lines = f.readlines()
        for i, line in enumerate(lines):
            if gk in line and line[0]=='#':
                lines[i] = line[2:]
                flag = True
        f.close()

        if flag:
            f = open(file_path, "w")
            f.writelines(lines)
            f.close()
