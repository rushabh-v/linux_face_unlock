#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import sys
import os.path
import time
import os

for i in sys.path:
    if os.path.isfile(i+"/cv2/data/haarcascade_frontalface_default.xml"):
        face_detector = cv2.CascadeClassifier(i+'/cv2/data/haarcascade_frontalface_default.xml') 
        break

def getFaces(training=False):
    
    saved=False
    start_time = time.time()
    cap = cv2.VideoCapture(0)
    ti = time.time()-start_time
    k=0
    
    while ti<50:
        if ti>k and ti<k+1:
            saved = False
            
        ti = time.time()-start_time
        rat, img = cap.read()
        if training:
            cv2.imshow("Try to change angle and distance of your face from camera.",img)
        
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = face_detector.detectMultiScale(img, 1.3, 5)
        imgs = []
        for (x,y,w,h) in faces:
            imgs.append(img[y:y+h,x:x+w])
        if training:
            if len(imgs)==1:
                if saved==False:
                    cv2.imwrite("./images/Train/"+str(k)+".jpeg", imgs[0])
                    saved=True
                    k+=1        
        else:
            if len(imgs)!=0:
                cap.release()
                cv2.destroyAllWindows()
                return imgs
            
            else:
                if k==50:
                    raise Exception("No faces detected.")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return imgs            
            
    cap.release()
    cv2.destroyAllWindows()
    return imgs


