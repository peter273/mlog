# from MineLog.Equipment import Equipment,mload
# from MineLog.ShiftFile import ShiftFile
import pandas
from matplotlib import ticker
import matplotlib.pyplot as plt


#Plots the Utilization, Availability, Efficiency with respect to the dates
def oeeEquipmentPlot(eq):

    def format_coord(x,y):
        xid=int(x)
        nx= g.Date.iloc[xid].strftime("%b %d,%Y")
        shiftno=g.Shift.iloc[xid]
        util=round(g.Utilization.iloc[xid],2)
        avail=round(g.Availability.iloc[xid],2)
        ef=round(g.Efficiency.iloc[xid],2)
        oee=round(g.OEE.iloc[xid],2)
        
        datestr='Date={0} Shift{1}\n'
        availstr='Av={2}% '
        utilstr='Ut={3}% '
        efstr = 'Ef={4}% '
        oeestr='OEE = {5}% '

        out=''.join([datestr,availstr,utilstr,efstr,oeestr])
        return out.format(nx,shiftno,avail,util,ef,oee)
    def myformater(x,p):
        try:
            if g.Shift.iloc[int(x)] == '1':
                return str(g.Date.iloc[int(x)].day)
            else:
                return ''
        except:
            print(x)
            return ''

    g=pandas.DataFrame(eq.Data[['Shift','Date','Availability','Utilization','Efficiency','OEE']])
    fig,ax1=plt.subplots()
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(myformater))
    ax1.format_coord = format_coord

    g.plot(ax=ax1)
    plt.draw()
    plt.legend(loc='best')
    plt.show()
