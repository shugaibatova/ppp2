# Write a Python program to subtract five days from current date.
import datetime
def day(today):
    past=today.day-5
    return past
now = datetime.datetime.now()


print(day(now))