# from MineLog.Equipment import Equipment,mload
# from MineLog.ShiftFile import ShiftFile
import pandas
import datetime
from matplotlib import ticker
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def oeeEquipmentPlot(eq_list,param=['OEE','Availability','Utilization','Efficiecy'],
        data_frame='shiftly',export_data= False,marker='o',**kwargs):
    return Moving_AveragePlot(eq_list,param,
            data_frame=data_frame,
            export_data=export_data,
            interval=1,
            marker=marker,
            rolling=False,
            **kwargs)

# **kwargs are for plotting parameters
def Moving_AveragePlot(eq_list,param,data_frame="shiftly",
        export_data=False,interval=1,marker='o',rolling=True,**kwargs):

    g=getPlot_data(eq_list,data_frame,"Availability","Utilization","Efficiency","OEE",'totaltime')
    rolling_g={i:mrolling_mean(g[i],interval) for i in g}
    g=pandas.Panel.from_dict(rolling_g)

    plot_dict={i:[] for i in param}

    for par in param:
        plot_dict[par]=g.minor_xs(par)

    if export_data:
        return plot_dict

    if len(param)>1:
        fig,ax1=plt.subplots(len(param),1)
        axf=lambda i:ax1[i]
    else:
        fig,ax1=plt.subplots()
        axf=lambda i:ax1
    if rolling:
        titlex=lambda i:"{0} (rolling mean),I={1}".format(i,interval)
    else:
        titlex=lambda i:i

    for i,par in enumerate(param):
        k=plot_dict[par]
        temp=k.plot(
            ax=axf(i),
            title=titlex(par),
            marker=marker,
            **kwargs)
        if len(param)>1:
            temp.xaxis.label.set_visible(False)
    plt.subplots_adjust(hspace=.6)
    plt.draw()
    plt.show()
    return plot_dict

def mrolling_mean(df,interval):
    start,end=interval-1,len(df)
    val_weights={
            'Utilization':['Availability','totaltime'],
            'Availability':['totaltime'],
            'Efficiency':['totaltime'],
            'totaltime':[]
            }
    new_df = pandas.DataFrame.from_dict(mrolling_mean_helper(df,interval,val_weights))
    new_df['OEE'] = (new_df['Availability'] * new_df['Utilization'] *\
            new_df['Efficiency'])/(100**2)
    new_df['totaltime']=new_df['totaltime']*interval
    new_df.index=df.index[start:end]
    return new_df
    
# returns a rolling mean as a dictionary of the column headers
def mrolling_mean_helper(df,interval,val_weights={}):
    '''
    df:pandas dataframe, interval: integer, val_weights:dictionary
    val_weights example: value:[weights]
        {
        'Utilization':['Availability','totaltime'],
        'Availabiliy':['totaltime']
        }
    '''
    start,end=interval-1,len(df)
    a={i:[] for i in val_weights}
    for i in range(start,end):
        temp_df=df.iloc[i-(interval-1):i+1]
        for p in val_weights:
            numerator = temp_df[p]
            denominator = temp_df[p]
            for wi in val_weights[p]:
                numerator = numerator * temp_df[wi]
                denominator = denominator * temp_df[wi]
            denominator=denominator/temp_df[p]
            if len(val_weights)==0:
                a[p].append(temp_df[p].sum()/len(temp_df[p]))
            else:
                a[p].append(numerator.sum()/denominator.sum())
    return a

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

# Applies to Utilization and Availability only 
# TODO Efficiency weighted Average
def weighted_average(data_values,params,tt):
    if params=='Utilization':
        numerator=(data_values['Utilization'] * data_values['Availability']\
                *data_values[tt]).sum()
        denominator=(data_values['Availability']*data_values[tt]).sum()
    else:
        # params='Availability' or 'Efficiency'
        numerator=(data_values[params] * data_values[tt]).sum()
        denominator=data_values[tt].sum()
    return numerator/denominator


def get_tframe(
        eq,data_frame='shiftly',
        params=[
            "Availability",
            "Utilization",
            "Efficiency",
            "OEE",
            "totaltime"]):
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
        daily_data=g.groupby(['year','month','day'])
        daily=daily_data[params].mean()

        for i in ['Availability','Utilization','Efficiency']:
            daily[i]=daily_data.apply(weighted_average,i,'totaltime')
        daily['OEE']=(daily['Availability']*daily['Utilization']*daily['Efficiency'])/(100**2)
        daily['totaltime']=daily_data['totaltime'].sum()

        daily_index={'Date':[]}
        for i in daily.index:
            daily_index['Date'].append(datetime.datetime(*i))
        daily.index=pandas.DataFrame(daily_index)['Date']
        return daily
    elif data_frame=='weekly':
        weekly_data=g.groupby(['year','week'])
        weekly=weekly_data[params].mean()

        for i in ['Availability','Utilization','Efficiency']:
            weekly[i]=weekly_data.apply(weighted_average,i,'totaltime')
        weekly['OEE']=(weekly['Availability']*weekly['Utilization']*weekly['Efficiency'])/(100**2)
        weekly['totaltime']=weekly_data['totaltime'].sum()
        
        weekly_index={'Date':[]}
        for i in weekly.index:
            k=isocal_to_date(i[0],i[1],1)
            weekly_index['Date'].append(isocal_to_date(i[0],i[1],1))
        weekly.index=pandas.DataFrame(weekly_index)['Date']
        return weekly
    elif data_frame=='monthly':
        monthly_data=g.groupby(['year','month'])
        monthly = monthly_data[params].mean()

        for i in ['Availability','Utilization','Efficiency']:
            monthly[i]=monthly_data.apply(weighted_average,i,'totaltime')
        monthly['OEE']=(monthly['Availability']*monthly['Utilization']*monthly['Efficiency'])/(100**2)
        monthly['totaltime']=monthly_data['totaltime'].sum()

        monthly_index={'Date':[]}
        for i in monthly.index:
            monthly_index['Date'].append(datetime.datetime(i[0],i[1],1))
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

    



# Beta
# --------------------------------------------------

#TODO Pie Chart Plot for shiftfile
def pi_shift_plot(sffile):
    pass

def oeeEquipmentPlotbeta(eq_list,param=['OEE'],data_frame='shiftly',export_data= False,marker='o',**kwargs):
    g=getPlot_data(eq_list,data_frame,"Availability","Utilization","Efficiency","OEE")
    plot_dict = {i:None for i in param}

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
def Moving_AveragePlotbeta(eq_list,param,data_frame="shiftly",export_data=False,interval=2,marker='o',**kwargs):
    g=getPlot_data(eq_list,data_frame,"Availability","Utilization","Efficiency","OEE")

    plot_dict={i:[] for i in param}
    if len(param)>1:
        if not export_data:
            fig,ax1=plt.subplots(len(param),1)
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            plot_dict[par]=k
            if not export_data:
                temp=k.plot(
                        ax=ax1[i],
                        title=par+" (rolling mean),I={0}".format(interval),
                        marker=marker,
                        **kwargs)
                temp.xaxis.label.set_visible(False)
    else:
        if not export_data:
            fig,ax1=plt.subplots()
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            plot_dict[par]=k
            if not export_data:
                k.plot(
                    ax=ax1,
                    title=par+" (rolling mean),I={0}".format(interval),
                    marker=marker,
                    **kwargs)
    if not export_data:
        plt.subplots_adjust(hspace=.6)
        plt.draw()
        plt.show()
    return plot_dict

def mrolling_beta(df,interval,param=['Availability','Utilization','Efficiency','totaltime']):
    start=interval-1
    end = len(df)
    a={i:[] for i in param}
    for i in range(start,end):
        temp_df=df.iloc[i-(interval-1):i+1]
        avail = temp_df['Availability']
        eff = temp_df['Efficiency']
        utili = temp_df['Utilization']
        totaltime= temp_df['totaltime']

        a_numerator = (avail*totaltime).sum()
        a_denominator = totaltime.sum()
        a['Availability'].append(a_numerator/a_denominator)

        e_numerator = (eff*totaltime).sum()
        e_denominator = totaltime.sum()
        a['Efficiency'].append(e_numerator/e_denominator)

        u_numerator = (utili*avail*totaltime).sum()
        u_denominator = (avail*totaltime).sum()
        a['Utilization'].append(u_numerator/u_denominator)

        a['totaltime'].append(totaltime.sum())

    new_df = pandas.DataFrame.from_dict(a)
    new_df['OEE'] = (new_df['Availability'] * new_df['Utilization'] *\
            new_df['Efficiency'])/(100**2)
    new_df.index= df.index[start:end]

    return new_df
