import getFaces
from os import listdir
from os.path import isfile, join
from face_recognition import compare_faces
import numpy as np


def load_npy(file):
    return list(np.load(file))

def authenticate():
    
    path = '/lib/Auth/RecFace/roots/'
    roots = [(path+f) for f in listdir(path) if isfile(join(path, f))] 
    if not roots:
        return False
    roots = list(map(load_npy, roots))
    face_codes = getFaces.getFaces()

    if not face_codes:
        return False

    for code in face_codes:
        matches = np.array(compare_faces(roots, code))
        if matches.any():
            return True
    return False
