#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastai.vision import *
import cv2
from os import listdir
from os.path import isfile, join

class Training():
    def getDataBunch(self, tfm = True, val_p = 0, sz = 224, b_sz = 8):

        if tfm:
            data = ImageDataBunch.from_folder('./images/',
                                              ds_tfms=get_transforms(do_flip=False),
                                              valid_pct=val_p,
                                              size=sz,
                                              bs=b_sz)

        else:
            data = ImageDataBunch.from_folder('./images/',
                                              ds_tfms=None,
                                              valid_pct=val_p,
                                              size=sz,
                                              bs=b_sz)

        return data


    def train(self):
        
        path = './images/models/'
        root_models = [f for f in listdir(path) if isfile(join(path, f))]
        a = len(root_models)
        
        data = self.getDataBunch(val_p = 0)
        data.normalize(imagenet_stats)
        
        learn = create_cnn(data, models.vgg16_bn)
        
        learn.fit_one_cycle(4, 8e-3)
        learn.unfreeze()
        learn.fit_one_cycle(4, 6e-5)
        learn.fit_one_cycle(4, 1e-6)
        learn.save('root-'+str(a))

