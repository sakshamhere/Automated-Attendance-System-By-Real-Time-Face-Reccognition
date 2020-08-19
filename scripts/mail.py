import smtplib
import numpy as np
import pandas as pd
import os
import csv
import cv2
from time import sleep


#Please change the data file as the mails present in file are of real people!!!!!
#Please change the data file as the mails present in file are of real people!!!!!
#Please change the data file as the mails present in file are of real people!!!!!

def send_mail_student(sender,reciever,mail_body,mail_subject):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
    server.starttls() #encrypts are connection
    server.ehlo()

    server.login('your email','your pass') # put your email pass 
                                            #turn on -> https://myaccount.google.com/lesssecureapps

    subject = mail_subject
    body = mail_body

    msg = f"Subject: {subject}\n\n{body}" #new f-string way to format in python like we use ``  and ${} in js
    
    server.sendmail(
        sender, #from
        reciever, #to
        msg
    )
    print('mail sent!')
    server.quit()

def send_mail(line):
    print(line)
    print(line)
    sender = 'your email' # put your email
    reciever = line[3] #Please change the data file as the mails present in file are of real people!!!!!
    mail_body = 'Your Attendance has been marked, current attendance 74%'
    mail_subject = 'Attendance notification'
    send_mail_student(sender,reciever,mail_body,mail_subject)





def mail(sem,sec):
    print(sem,sec)
    if sem == '1' or sem == '2':
        year = 'first_year'
    elif sem == '3' or sem == '4':
        year = 'second_year'
    elif sem == '5' or sem == '6':
        year = 'third_year'
    else:
        year = 'fourth_year'
    filename = f'data/excel/{year}/{year}_{sem}sem_IT{sec}.xlsx'


    def from_excel_to_csv():
        df = pd.read_excel(filename,index=False)
        df.to_csv('./current.csv')

    def getdata_details():
        details,roll = getdata()
        #print('Mail sended to',l)

        with open('./current.csv','r') as f:
            data = csv.reader(f)
            next(data)
            lines = list(data)
            for line in lines:
                for i in line:
                    if i in roll:
                        print(i)
                        for detail in details:
                            if i in detail:
                                send_mail(line)
                #print(line)
                

    def getdata():
        l=[]
        roll=[]
        with open('./data.csv','r') as f:
            data = csv.reader(f)
            next(data)
            lines = list(data)
            for line in lines:
                if line[-1]=='1':
                    l.append(line)
                    roll.append(line[1])
                    #print(line[1])
        
        
        return l,roll
    from_excel_to_csv()
    getdata_details()