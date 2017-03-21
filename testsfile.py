from MineLog import *

import os
# from datetime import datetime as dt
import datetime

filepath=os.path.dirname(__file__)
x=ShiftFile(os.path.join(filepath,"MineLog/datagenerator_output/Equipment1_20170320_Shift2.txt"))
# print(x.day)
# print("Week",x.week)


def isocal_to_datetime(year, week, day):
    jan4 = datetime.date(year, 1, 4)
    start = jan4 - datetime.timedelta(days=jan4.isoweekday()-1)
    return start + datetime.timedelta(weeks=week-1, days=day-1)

print(x.Date.isocalendar())
print(isocal_to_datetime(*list(x.Date.isocalendar())))
# print(x.Date.year)
# print(x.Date.month)
# print(x.Date.day)
# print("day",x.day)
# print(datetime(x.Date.year,x.Date.month,x.Date.day))


#returns week number
# print("week number",x.Date.isocalendar()[1])

# print(x.data)
