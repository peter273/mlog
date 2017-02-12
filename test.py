from MineLog import Equipment,ShiftFile,mload
import pandas
import matplotlib.pyplot as plt
import os
import time


start = time.time()
# x=Equipment("Equipment1")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save()

y=mload('Equipment1.mlog')
y.update()
end= time.time()
# print(end-start)

# print(y.Data)
end= time.time()
print(end-start)

g=y.Data[['Shift','Date','Availability','Utilization','Efficiency','OEE']]

def format_coord(x,y):
    xid=int(x)
    nx= g.Date.iloc[xid].strftime("%b %d,%Y")
    shiftno=g.Shift.iloc[xid]
    util=round(g.Utilization.iloc[xid],2)
    avail=round(g.Availability.iloc[xid],2)
    ef=round(g.Efficiency.iloc[xid],2)
    oee=round(g.OEE.iloc[xid],2)

    datestr='Date={0} Shift{1}\n'
    availstr='Availability={2}%\n'
    utilstr='Utilization={3}%\n'
    efstr = 'Efficiency={4}%\n'
    oeestr='OEE = {5}%'

    out=''.join([datestr,availstr,utilstr,efstr,oeestr])
    return out.format(nx,shiftno,avail,util,ef,oee)
    
fig,ax1=plt.subplots()
ax1.format_coord = format_coord
g.plot(ax=ax1)

plt.legend(loc='best')
plt.show()


        


