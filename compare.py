import getFaces
from cv2 import resize, imwrite, INTER_AREA
from fastai.vision import ImageDataBunch, cnn_learner, imagenet_stats, models, open_image
from os import listdir
from os.path import isfile, join

def compare(root_n, img, learn):
    learn.load(root_n)
    if str(learn.predict(img)[0])=="Train":
        return True
    else:
        return False
    
def authenticate():
    
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
    learn = cnn_learner(data, models.resnet34)
    
    imgs = getFaces.getFaces()
    if len(imgs)==0:
        return False
    
    for img in imgs:
        img = resize(img, (224,224), interpolation = INTER_AREA)
        imwrite('temp.jpeg', img)
        img = open_image('temp.jpeg')
        for mod in root_models:
            if compare(mod.split('.')[0], img, learn):
                return True
    return False
