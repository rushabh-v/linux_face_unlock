from os import listdir
from os.path import isfile, join

import numpy as np
from face_recognition import face_distance

import getFaces


def load_npy(file):
    return list(np.load(file))

def authenticate():
    
    path = '/lib/Auth/Facerec/roots/'
    roots = [(path+f) for f in listdir(path) if isfile(join(path, f))] 
    if not roots:
        return False
    roots = list(map(load_npy, roots))
    face_codes = getFaces.getFaces()

    if not face_codes:
        return False

    for code in face_codes:
        distances = np.array(face_distance(roots, code))
        matches = distances < 0.35
        if matches.any():
            return True
    raise Exception("facerec did not recognize any face! Please enter the password.")
