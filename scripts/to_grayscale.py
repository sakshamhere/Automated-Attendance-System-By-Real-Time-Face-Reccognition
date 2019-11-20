import cv2
import os
import numpy as np

#This module resizes image from a given directory to 100*100 pixels and writes all images to given directory
count=0
if not os.path.exists('../gray_images'):
    os.makedirs('../gray_images')

for path, subdirnames, filenames in os.walk("../dataset"):
    for dir in subdirnames:
        if not os.path.exists(f'../gray_images/{str(dir)}'):
            os.makedirs(f'../gray_images/{str(dir)}')
            filenames = os.listdir(f'../dataset/{str(dir)}')
            print(filenames)
            for filename in filenames:
                if filename.startswith("."):
                    print("Skipping File:",filename)#Skipping files that startwith .
                    continue
                print(path,filename)
                #img_path=os.path.join(path, filename)#fetching image path
                img_path = f'../dataset\{str(dir)}\{filename}'
                print("img_path",img_path)

                facedata = "../haarcascade/haarcascade_frontalface_default.xml"
                cascade = cv2.CascadeClassifier(facedata)
                img = cv2.imread(img_path)
                
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # minisize = (img.shape[1],img.shape[0])
                # miniframe = cv2.resize(img, minisize)
                 
                faces = cascade.detectMultiScale(gray,1.3,5)

                for f in faces:
                    x, y, w, h = [ v for v in f ]
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                    sub = img[y:y+h, x:x+w]
                
                
                gray = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY) 
                equ = cv2.equalizeHist(gray) 
                final = cv2.medianBlur(equ, 3)
    
                new_path=f"../gray_images/{str(dir)}"

                print("desired path is",f'../gray_images/{str(dir)}/frame{count}.jpg')#write all images to resizedTrainingImages/id directory
                cv2.imwrite(f'../gray_images/{str(dir)}/frame{count}.jpg',final)
                count += 1




