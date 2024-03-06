# Write a Python program to print yesterday, today, tomorrow.
import datetime
today=datetime.datetime.now()
yesterday=(today.day-1)
tomorrow=today.day+1
print(yesterday)
print(today)
print(tomorrow)