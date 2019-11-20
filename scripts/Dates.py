import calendar 
import datetime
import holidays

def filterdates():
    def holiday():
        holy=[]

        for date in sorted(holidays.IND(years=2019).items()):
            holy.append(date[0])
        return holy


    now = datetime.datetime.now()
    dt=[]

    year=now.year
    obj = calendar.Calendar() 


    for month in range(1,13):
        for day in obj.itermonthdates(year,month):
            
            if day.strftime("%A") == 'Saturday' or day.strftime("%A") == 'Sunday' or day in holiday():
                pass
        
            else:
                
                dt.append(day)
    return dt

