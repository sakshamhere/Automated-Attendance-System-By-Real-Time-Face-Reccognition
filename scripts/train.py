# lets import the required packages 
import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create() # instantiate the lbph recognizer


path = '../gray_images' #setting out path of folders with images


if not os.path.exists('../recognizer'):
    os.makedirs('../recognizer') # making a directory for yml file which will be generated after training

def getImageswithId(path):
    faces = []
    faceid = []

    for root,directory,filenames in os.walk(path):
        for filename in filenames:
            id = os.path.basename(root) #this directly assigns folder name ie 0,1..
            img_path = os.path.join(root,filename)
            print('img_path:',img_path)
            print('id:',id)
            test_img = cv2.imread(img_path)
           
            # test_img = np.float32(test_img)
            if test_img is None:
                print('image not loaded poperly - cv2 cant read!!')
                continue
            #if images in dataset are not in gray scale then use below 3 line

            gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale
            face_haar_cascade=cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')#Load haar classifier
            face=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)#detectMultiScale returns rectangles
           
            if len(face)!=1:
                continue # since we are asuuming only single person images are being fed to classifier

            (x,y,w,h) = face[0]
            gray = gray_img[y:y+h,x:x+h]
            equ = cv2.equalizeHist(gray) 
            final = cv2.medianBlur(equ, 3)
            faces.append(final)
            faceid.append(int(id))

    return faceid,faces


faceid , faces = getImageswithId(path)
recognizer.train(faces,np.array(faceid))
recognizer.save('../recognizer/trainingData.yml')
cv2.destroyAllWindows()
