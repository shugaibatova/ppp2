
#  Write a Python program to calculate two date difference in seconds.
import datetime
def diff(dt1,dt2):
    delta=dt2-dt1
    return delta.days*24*3600+delta.seconds
mybirth=datetime.datetime(2006,5,27,12,20,31)
today=datetime.datetime.now()
print(diff(mybirth,today))