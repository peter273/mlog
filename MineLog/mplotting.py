# from MineLog.Equipment import Equipment,mload
# from MineLog.ShiftFile import ShiftFile
import pandas
import datetime
from matplotlib import ticker
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def oeeEquipmentPlot(eq_list,param=['OEE'],data_frame='shiftly',export_data=False,marker='o',**kwargs):
    g=getPlot_data(eq_list,data_frame,"Availability","Utilization","Efficiency","OEE")
    plot_dict={i:None for i in param}
    if len(param)>1:
        if not export_data:
            fig,ax1=plt.subplots(len(param),1)
        for i,par in enumerate(param):
            k=g.minor_xs(par)
            plot_dict[par]=k
            if not export_data:
                temp=k.plot(ax=ax1[i],title=par,marker=marker,**kwargs)
                temp.xaxis.label.set_visible(False)
    else:
        if not export_data:
            fig,ax1=plt.subplots()
        for i,par in enumerate(param):
            k=g.minor_xs(par)
            plot_dict[par]=k
            if not export_data:
                k.plot(ax=ax1,title=par,marker=marker,**kwargs)
    if not export_data:
        plt.subplots_adjust(hspace=.6)
        plt.draw()
        plt.show()
    return plot_dict

# **kwargs are for plotting parameters
def Moving_AveragePlot(eq_list,param,data_frame="shiftly",export_data=False,interval=2,marker='o',**kwargs):
    g=getPlot_data(eq_list,data_frame,"Availability","Utilization","Efficiency","OEE")
    plot_dict={i:[] for i in param}
    if len(param)>1:
        if not export_data:
            fig,ax1=plt.subplots(len(param),1)
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            plot_dict[par]=k
            if not export_data:
                temp=k.plot(ax=ax1[i],title=par+" (rolling mean),I={0}".format(interval),marker=marker,**kwargs)
                temp.xaxis.label.set_visible(False)
    else:
        if not export_data:
            fig,ax1=plt.subplots()
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            plot_dict[par]=k
            if not export_data:
                k.plot(ax=ax1,title=par+" (rolling mean),I={0}".format(interval),\
                        marker=marker,**kwargs)
    if not export_data:
        plt.subplots_adjust(hspace=.6)
        plt.draw()
        plt.show()
    return plot_dict
#for oeeEquipmentPlot and MovingAveragePlot
def getPlot_data(eq_list,data_frame='shiftly',*param):
    g={}
    iparam=['Date']
    iparam.extend(list(param))

    for i in eq_list:
        g[i.Name] = get_tframe(i,data_frame,list(param))
        # g[i.Name] = i.Data[iparam]
        # g[i.Name].index=g[i.Name]['Date']
    return pandas.Panel.from_dict(g)

def get_tframe(eq,data_frame='shiftly',params=["Availability","Utilization","Efficiency","OEE"]):
    g=eq.Data
    tframe={"week":[],"day":[],"month":[],"year":[]}
    for index,row in g['Date'].iteritems():
        tframe['week'].append(row.isocalendar()[1])
        tframe['month'].append(row.month)
        tframe['year'].append(row.year)
        tframe['day'].append(row.day)
    for i in tframe:
        g[i]=pandas.Series(tframe[i])
    g=g.drop(['EType','data'],axis=1)

    if data_frame=='daily':
        daily=g.groupby(['year','month','day']).mean()[params]
        daily_index={'Date':[]}
        for i in daily.index:
            daily_index['Date'].append(datetime.datetime(*i))
        daily.index=pandas.DataFrame(daily_index)['Date']
        return daily
    elif data_frame=='weekly':
        weekly=g.groupby(['year','week']).mean()[params]
        weekly_index={'Date':[]}
        for i in weekly.index:
            k=isocal_to_date(*i,1)
            weekly_index['Date'].append(isocal_to_date(*i,1))
        weekly.index=pandas.DataFrame(weekly_index)['Date']
        return weekly
    elif data_frame=='monthly':
        monthly=g.groupby(['year','month']).mean()[params]
        monthly_index={'Date':[]}
        for i in monthly.index:
            monthly_index['Date'].append(datetime.datetime(*i,1))
        monthly.index=pandas.DataFrame(monthly_index)['Date']
        return monthly
    else:
        shiftly=g[params]
        shiftly.index=g['Date']
        return shiftly
#convert isocalendar datetime object
def isocal_to_date(year, week, day=1):
    jan4 = datetime.datetime(year, 1, 4)
    start = jan4 - datetime.timedelta(days=jan4.isoweekday()-1)
    return start + datetime.timedelta(weeks=week-1, days=day-1)

#TODO Pie Chart Plot for shiftfile
def pi_shift_plot(sffile):
    pass
    



