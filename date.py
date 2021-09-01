from datetime import date  
date1=date.today()
date2=date(2021,4,20)
print(date2)
if(date1>date2):
    d=date1-date2
    print(d)
else:
    d=date2-date
    print(d)