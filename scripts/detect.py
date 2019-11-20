import numpy as np
import pandas as pd
import os
import csv
import cv2
from time import sleep


def detect():
    filename = 'data/Attendance_xlsx/third_year_5sem_IT2.xlsx'

    fname = 'recognizer/trainingData.yml'
    if not os.path.isfile(fname):
        print('first train the data')
        exit(0)


    names = {}
    labels = []
    students = []


    def from_excel_to_csv():
        df = pd.read_excel(filename,index=False)
        df.to_csv('./data.csv')

    def getdata():
        with open('data.csv','r') as f:
            data = csv.reader(f)
            next(data)
            lines = list(data)
            for line in lines:
                names[int(line[0])] = line[1]


    def  markPresent(name):
        with open('data.csv','r') as f:
            data = csv.reader(f)
            lines = list(data)
            # for line in lines:
            #     line.pop(0)
            # print(lines)
            for line in lines:
                if line[1] == name:
                    line[-1] = '1'
                    with open('data.csv','w') as g:
                        writer = csv.writer(g,lineterminator='\n')
                        writer.writerows(lines)
                        break
        
        # df = pd.read_csv('data.csv')
        # df.to_excel('data.xlsx',index=False)

    def update_Excel():
        with open('data.csv') as f:
            data = csv.reader(f)
            lines = list(data)
            for line in lines:
                line.pop(0)
            with open('data.csv','w') as g:
                writer = csv.writer(g,lineterminator='\n')
                writer.writerows(lines)
                
        df = pd.read_csv('data.csv')
        df.to_excel('data.xlsx',index = False)
        

    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture('test_videos/test3101.mp4')

    # cap.set(3,640) # set Width
    # cap.set(4,480) # set Height

    from_excel_to_csv() # converting the excel to csv for use
    getdata() # getting the data from csv in a dictionary
    print('Total students :',names)

    recognizer = cv2.face.LBPHFaceRecognizer_create() #LOCAL BINARY PATTERNS HISTOGRAMS Face Recognizer

    recognizer.read(fname) # read the trained yml file

    num=0
    while True:   
        ret, img = cap.read()
        #img = cv2.rotate(img, rotateCode=cv2.ROTATE_90_CLOCKWISE)
        #img = cv2.rotate(img, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray) 
        final = cv2.medianBlur(equ, 3)

        faces = face_cascade.detectMultiScale(final, 1.3, 5)
        

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            label,confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print('label:',label)
            print('confidence:',confidence)
            predicted_name = names[label]
            if confidence < 90:
                confidence = 100 - round(confidence)
                cv2.putText(img, predicted_name +str(confidence) +'%', (x+2,y+h-4), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
                labels.append(label)
                students.append(names[label])
                totalstudents = set(students)
                justlabels = set(labels)
                print('student Recognised : ',totalstudents,justlabels)
                for i in justlabels:
                    if labels.count(i)>20:
                        markPresent(names[label])
    
            

            
            
            
            cv2.imshow('Face Recognizer',img)
            k = cv2.waitKey(30) & 0xff
            # if cv2.waitKey(33) == ord('a'):
            num+=1
            if num>100:
                cap.release()
                sleep(4)
                print('we are done!')
                
                break
        



    #cv2.destroyAllWindows()

