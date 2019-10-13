#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getFaces
import cv2
from fastai.vision import ImageDataBunch, create_cnn, open_image
from os import listdir
from os.path import isfile, join

def compare(root_n, img, learn):
    learn.load(root_n)
    if str(learn.predict(img)[0])=="Train":
        return True
    else:
        return False
    
def authenticate(pamh):
    
    path = './images/models/'
    root_models = [f for f in listdir(path) if isfile(join(path, f))]
    print(root_models)
    if 'tmp.pth' in root_models:
        root_models.remove('tmp.pth')
        
    classes = ["Test", "Train"]
    data = ImageDataBunch.single_from_classes('./images/', 
                                               classes, 
                                               ds_tfms=None, 
                                               size = 224)
    
    
    data.normalize(imagenet_stats)
    learn = create_cnn(data, models.vgg16_bn)
    
    imgs = getFaces.getFaces()
    if len(imgs)==0:
        return pamh.PAM_SYSTEM_ERR
        #return False
    
    for img in imgs:
        img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
        cv2.imwrite('temp.jpeg', img)
        img = open_image('temp.jpeg')
        for mod in root_models:
            if compare(mod.split('.')[0], img, learn):
                return pamh.PAM_SUCCESS
                #return True
    return pamh.PAM_AUTH_ERR
    #return False
    
def pam_sm_authenticate(pamh, flags, args):
    return authenticate(pamh)

def pam_sm_open_session(pamh, flags, args):
    return authenticate(pamh)

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS

