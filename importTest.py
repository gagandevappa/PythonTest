import gagan_package as gp
import sys
import random
import datetime,calendar

gp.welcomeMessage()

courses=['python','java','nodejs','R','mongoDB']
target1='nodejs'
target2='PLSQL'
indexVal1=gp.findIndex(courses,target1)
indexVal2=gp.findIndex(courses,target2)
print(indexVal1)
print(indexVal2)
print(gp.testVal)
#print(sys.path)
ranChoice=random.choice(courses)
print(ranChoice)
todayID=datetime.date.today()
print(todayID)
time=datetime.time(22,10,55).hour
print(time)
leapyear=calendar.isleap(2017)
leapyear2=calendar.isleap(2020)
print('2017: ',leapyear,' 2020: ',leapyear2)
print('The random libraray path is: ',random.__file__)