import datetime
import time
import math
dob = datetime.datetime(2006,11,3)
today = datetime.datetime.today()
age = today - dob
print (age)
a = datetime.timedelta(days = 365)
print (a)
b = age/a
print (b)

years = math.floor(b)
months = (b - years)*12
print ("I am %3.2f years and %f months old" %(years, months))
