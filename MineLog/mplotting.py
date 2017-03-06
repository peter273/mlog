# from MineLog.Equipment import Equipment,mload
# from MineLog.ShiftFile import ShiftFile
import pandas
from matplotlib import ticker
import matplotlib.pyplot as plt
plt.style.use('ggplot')


#Plots the Utilization, Availability, Efficiency with respect to the dates
def oeeEquipmentPlot(eq,marker='o'):

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
                return g.Date.iloc[int(x)].strftime('%b %d')
                # return str(g.Date.iloc[int(x)].month)+str(g.Date.iloc[int(x)].day)
            else:
                return ''
        except:
            # print(x)
            return ''

    g=pandas.DataFrame(eq.Data[['Shift','Date','Availability','Utilization','Efficiency','OEE']])
    fig,ax1=plt.subplots()
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(myformater))
    ax1.format_coord = format_coord

    g.plot(ax=ax1,marker=marker,title=eq.Name)
    plt.legend(loc='best')
    plt.draw()
    plt.show()

def oeeEquipmentPlot1(eq):

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
                return g.Date.iloc[int(x)].strftime('%b %d')
                # return str(g.Date.iloc[int(x)].month)+str(g.Date.iloc[int(x)].day)
            else:
                return ''
        except:
            print(x)
            return ''

    g=pandas.DataFrame(eq.Data[['Shift','Date','Availability','Utilization','Efficiency','OEE']])
    g.index=g['Date']
    fig,ax1=plt.subplots()
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(myformater))
    ax1.format_coord = format_coord

    g.plot(ax=ax1)
    plt.draw()
    plt.legend(loc='best')
    plt.show()

#for param_plot and MovingAveragePlot
def getPlot_data(eq_list,param):
    g={}

    for i in eq_list:
        g[i.Name] = i.Data[['Date',param]]
        g[i.Name].index=g[i.Name]['Date']
    return pandas.Panel.from_dict(g)
def param_plot(eq_list,param,marker='o'):
    # g={}
    # fig,ax1=plt.subplots()
    # ax1.xaxis.label.set_visible(False)

    # for i in eq_list:
    #     g[i.Name] = i.Data[['Date',param]]
    #     g[i.Name].index=g[i.Name]['Date']
    # g=pandas.Panel.from_dict(g)
    fig,ax1=plt.subplots()
    ax1.xaxis.label.set_visible(False)

    g=getPlot_data(eq_list,param)
    g=g.minor_xs(param)
    g.plot(ax=ax1,title=param,marker=marker)
    plt.draw()
    plt.show()
    return
# **kwargs are for plotting parameters
def Moving_AveragePlot(eq_list,param,interval=2,marker='o',**kwargs):
    fig,ax1=plt.subplots()
    ax1.xaxis.label.set_visible(False)

    g=getPlot_data(eq_list,param)
    g=g.minor_xs(param).rolling(window=interval).mean()
    g.plot(ax=ax1,title=param+"\n(Moving Average,interval={0})".format(interval),\
            marker=marker,**kwargs)
    plt.draw()
    plt.show()

def param_multiple_plot(eq_list,marker='o'):
    g={}
    fig,ax=plt.subplots(2,2)

    ax[0,0].xaxis.label.set_visible(False)
    ax[0,1].xaxis.label.set_visible(False)
    ax[1,0].xaxis.label.set_visible(False)
    ax[1,1].xaxis.label.set_visible(False)
    
    for i in eq_list:
        g[i.Name] = i.Data[['Date','OEE','Utilization','Availability','Efficiency']]
        g[i.Name].index=g[i.Name]['Date']

    g=pandas.Panel.from_dict(g)
    g.minor_xs('Utilization').plot(ax=ax[0,0],title='Utilization',marker=marker)
    g.minor_xs('Availability').plot(ax=ax[0,1],title='Availability',marker=marker)
    g.minor_xs('Efficiency').plot(ax=ax[1,0],title='Efficiency',marker=marker)
    g.minor_xs('OEE').plot(ax=ax[1,1],title='OEE',marker=marker)
    plt.draw()
    plt.tight_layout()
    plt.show()
#TODO Pie Chart Plot for shiftfile
def pi_shift_plot(sffile):
    pass
    


