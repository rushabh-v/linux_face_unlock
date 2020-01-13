#!/usr/bin/env python
# coding: utf-8

# In[8]:
from sys import path as syspath
from cv2 import CascadeClassifier, VideoCapture, imshow, imwrite, cvtColor, COLOR_BGR2GRAY, destroyAllWindows, waitKey
import os.path
import time

for i in syspath:
    if os.path.isfile(i+"/cv2/data/haarcascade_frontalface_default.xml"):
        face_detector = CascadeClassifier(i+'/cv2/data/haarcascade_frontalface_default.xml') 
        break

def getFaces(training=False):
    if(training):
        print("")
        print("There shold be only one person in frount of the camera while it takes the pictures to train the model on.")
        print("")
        print("It will take pictures for next 50 seconds press ENTER when ready: ")
        input()
    saved=False
    start_time = time.time()
    cap = VideoCapture(0)
    ti = time.time()-start_time
    k=0
    while ti<50:
        if ti>k and saved:
            saved = False
            
        ti = time.time()-start_time
        rat, img = cap.read()
        if training:
            imshow("Try to change angle and distance of your face from camera.",img)
        
            
        gray = cvtColor(img, COLOR_BGR2GRAY) 
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        imgs = []
        for (x,y,w,h) in faces:
            imgs.append(gray[y:y+h,x:x+w])
        if training:
            if len(imgs)==1:
                if saved==False:
                    k+=1
                    imwrite("/lib/Auth/RecFace/images/Train/"+str(k)+".jpeg", imgs[0])
                    saved=True       
        else:
            if len(imgs)!=0:
                cap.release()
                destroyAllWindows()
                return imgs
            
            else:
                if k==50:
                    raise Exception("No faces detected.")
        
        if waitKey(1) & 0xFF == ord('q'):
            cap.release()
            destroyAllWindows()
            return imgs          
            
    cap.release()
    destroyAllWindows()
    return imgs

