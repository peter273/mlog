from MineLog import Equipment,ShiftFile,mload, oeeEquipmentPlot,oeeEquipmentPlot1,param_plot
import numpy as np
import pandas
from matplotlib import ticker
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import datetime
import os
import pytz
import time

# print(y.Data)


# def format_coord(x,y):
#     xid=int(x)
#     nx= g.Date.iloc[xid].strftime("%b %d,%Y")
#     shiftno=g.Shift.iloc[xid]
#     util=round(g.Utilization.iloc[xid],2)
#     avail=round(g.Availability.iloc[xid],2)
#     ef=round(g.Efficiency.iloc[xid],2)
#     oee=round(g.OEE.iloc[xid],2)
    
#     datestr='Date={0} Shift{1}\n'
#     availstr='Av={2}% '
#     utilstr='Ut={3}% '
#     efstr = 'Ef={4}% '
#     oeestr='OEE = {5}% '

#     out=''.join([datestr,availstr,utilstr,efstr,oeestr])
#     return out.format(nx,shiftno,avail,util,ef,oee)

# g=pandas.DataFrame(y.Data[['Shift','Date','Availability','Utilization','Efficiency','OEE']])
# # g= pandas.DataFrame(y.Data,index=y.Data.Date)
# # g.index= g.Date
# # print(g.index.values)


# # print(datetime.datetime.strftime(g.Date.iloc[0]))
# # g=pandas.DataFrame(g,index=g.Date)
# # g=g.set_index(pandas.DatetimeIndex(g.Date))

# # print(type(g.Date.iloc[0]))
# # print(g.Date.iloc[0].strftime('%b %d,%Y')) # print(g.index) 

# # datafile = cbook.get_sample_data('goog.npy')
# # r = np.load(datafile, encoding='bytes').view(np.recarray)

# fig,ax1=plt.subplots()
# # ax1.plot(r.date,r.adj_close)

# # t=np.array([g.Date.iloc[i].to_pydatetime() for i in range(len(g.index))])

# # print(t)
# # print(type(g.Date.iloc[0]))

# ax1.format_coord = format_coord
# # ax1.plot(g.index,g.Utilization)

# # ax1.plot(g.index,g.Availability)
# # ax1.plot(g.index,g.OEE)

# def myformater(x,p):
#     try:
#         if g.Shift.iloc[int(x)] == '1':
#             return str(g.Date.iloc[int(x)].day)
#         else:
#             return ""
#     except:
#         print(x)
#         return ''

# # ax1.xaxis.set_major_locator(mdates.DayLocator())
# # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# # ax1.xaxis.set_minor_locator(mdates.HourLocator())
# # ax1.set_xlim(t.min(),t.max())

# # fig.autofmt_xdate()
# # ax1.set_xlim([0,len(g.index)-1])
# ax1.xaxis.set_major_formatter(ticker.FuncFormatter(myformater))

# g.plot(ax=ax1)

# plt.draw()
# plt.legend(loc='best')
# plt.show()


# # datemin = datetime.date(r.date.min().year, 1, 1)
# # datemax = datetime.date(r.date.max().year + 1, 1, 1)

# # ax1.format_xdata = mdates.DateFormatter('%b %d %Y')
# # ax1.grid(True)

# # print(end-start)



start = time.time()
x=Equipment("Equipment1")
x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
x.update()
x.save()
print(len(x.Data))


x=Equipment("Equipment2")
x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
x.update()
x.save()
print(len(x.Data))

x=Equipment("Equipment3")
x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
x.update()
x.save()
print(len(x.Data))

y1=mload('Equipment1.mlog')
y1.update()

y2=mload('Equipment2.mlog')
y2.update()

y3=mload('Equipment3.mlog')
y3.update()
# oeeEquipmentPlot(y)
param_plot([y1,y2,y3],'OEE')
param_plot([y1,y2,y3],'Utilization')
param_plot([y1,y2,y3],'Availability')

end= time.time()
print(end-start)
