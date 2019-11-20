import pandas as pd
import csv
import numpy as np
from scripts import mail as m


def mail():
    filename = 'data/excel/third_year_5sem_IT2.xlsx'


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
                                m.send_mail(line)
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



def updatef():
    filename = '/data/Attendance_xlsx/third_year_5sem_IT2.xlsx'
    with open('data.csv') as f:
        data = csv.reader(f)
        lines = list(data)
        if lines[1][0] == '0':
            
            for line in lines:
                line.pop(0)
            with open('data.csv','w') as g:
                writer = csv.writer(g,lineterminator='\n')
                writer.writerows(lines)
            
            df = pd.read_csv('data.csv')
            df.to_excel(filename,index = False)
            mail()

        else:
            print('Already Updated')


  

