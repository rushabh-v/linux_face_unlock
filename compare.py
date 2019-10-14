import getFaces
import cv2
from fastai.vision import *
from os import listdir
from os.path import isfile, join

def compare(root_n, img, learn):
    learn.load(root_n)
    if str(learn.predict(img)[0])=="Train":
        return True
    else:
        return False
    
def authenticate():
    print("Came")
    path = '/lib/Auth/RecFace/images/models/'
    root_models = [f for f in listdir(path) if isfile(join(path, f))]
    if 'tmp.pth' in root_models:
        root_models.remove('tmp.pth')
        
    classes = ["Test", "Train"]
    data = ImageDataBunch.single_from_classes('/lib/Auth/RecFace/images/', 
                                               classes, 
                                               ds_tfms=None, 
                                               size = 224)
    
    
    data.normalize(imagenet_stats)
    learn = cnn_learner(data, models.vgg16_bn)
    
    imgs = getFaces.getFaces()
    if len(imgs)==0:
        return False
    
    for img in imgs:
        img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
        cv2.imwrite('temp.jpeg', img)
        img = open_image('temp.jpeg')
        for mod in root_models:
            if compare(mod.split('.')[0], img, learn):
                return True
    return False
