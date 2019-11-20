import cv2
import os
import numpy as np

count=0
if not os.path.exists('./cropped_images'):
    os.makedirs('./cropped_images')

for path, subdirnames, filenames in os.walk("dataset"):
    for dir in subdirnames:
        if not os.path.exists(f'./cropped_images/{str(dir)}'):
            os.makedirs(f'./cropped_images/{str(dir)}')
            filenames = os.listdir(f'./dataset/{str(dir)}')
            print(filenames)
            for filename in filenames:
                if filename.startswith("."):
                    print("Skipping File:",filename)#Skipping files that startwith .
                    continue
                print(path,filename)
                #img_path=os.path.join(path, filename)#fetching image path
                img_path = f'dataset\{str(dir)}\{filename}'
                print("img_path",img_path)

                facedata = "haarcascade_frontalface_default.xml"
                cascade = cv2.CascadeClassifier(facedata)
                img = cv2.imread(img_path)
                minisize = (img.shape[1],img.shape[0])
                miniframe = cv2.resize(img, minisize)

                faces = cascade.detectMultiScale(miniframe)

                for f in faces:
                    x, y, w, h = [ v for v in f ]

                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                    sub_face = img[y:y+h, x:x+w]

                new_path=f"cropped_images/{str(dir)}"

                print("desired path is",f'./cropped_images/{str(dir)}/frame{count}.jpg')
                cv2.imwrite(f'./cropped_images/{str(dir)}/frame{count}.jpg',sub_face)
                count += 1




