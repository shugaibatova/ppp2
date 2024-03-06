# Write a Python program to drop microseconds from datetime.
import datetime
data=datetime.datetime.now()

print(data.strftime("%c"))