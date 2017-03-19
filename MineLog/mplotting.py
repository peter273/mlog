# from MineLog.Equipment import Equipment,mload
# from MineLog.ShiftFile import ShiftFile
import pandas
from matplotlib import ticker
import matplotlib.pyplot as plt
plt.style.use('ggplot')


#Plots the Utilization, Availability, Efficiency with respect to the dates
def oeeEquipmentPlot(eq,iparams=['Availability','Utilization','Efficiency','OEE'],marker='o'):

    def format_coord(x,y):
        xid=int(x)
        nx= g.Date.iloc[xid].strftime("%b %d,%Y")
        shiftno=g.Shift.iloc[xid]

        datestr='Date={0} Shift{1}\n'
        p_val=[round(getattr(g,elem).iloc[xid],2) for elem in iparams]
        p_str=[str_params[elem]+"={"+str(i+2)+"}% " for elem,i in zip(iparams,range(len(iparams)))]
        t=[datestr]
        t.extend(p_str)
        return ''.join(t).format(nx,shiftno,*p_val)

        
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

    str_params={'Availability':'Av','Utilization':'Ut','Efficiency':"Ef",'OEE':'OEE'}
    params=['Shift','Date']
    params.extend(iparams)

    g=pandas.DataFrame(eq.Data[params])
    fig,ax1=plt.subplots()
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(myformater))
    ax1.format_coord = format_coord

    g.plot(ax=ax1,marker=marker,title=eq.Name)
    plt.legend(loc='best')
    plt.draw()
    plt.show()

def oeeEquipmentPlot1(eq_list,param,marker='o',**kwargs):
    # params=['Date']
    # params.extend(iparams)

    # g=pandas.DataFrame(eq.Data[params])
    # g.index=g['Date']
    # fig,ax1=plt.subplots()

    # g.plot(ax=ax1,marker=marker,title=eq.Name)
    # plt.legend(loc='best')
    # plt.draw()
    # plt.show()

    g=getPlot_data(eq_list,"Availability","Utilization","Efficiency","OEE")
    if len(param)>1:
        fig,ax1=plt.subplots(len(param),1)
        for i,par in enumerate(param):
            k=g.minor_xs(par)
            temp=k.plot(ax=ax1[i],title=par,marker=marker,**kwargs)
            temp.xaxis.label.set_visible(False)
    else:
        fig,ax1=plt.subplots()
        for i,par in enumerate(param):
            k=g.minor_xs(par)
            k.plot(ax=ax1,title=par,marker=marker,**kwargs)
    plt.subplots_adjust(hspace=.6)
    plt.draw()
    plt.show()
#for param_plot and MovingAveragePlot
def getPlot_data(eq_list,*param):
    g={}
    iparam=['Date']
    iparam.extend(list(param))

    for i in eq_list:
        g[i.Name] = i.Data[iparam]
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
    g=getPlot_data(eq_list,"Availability","Utilization","Efficiency","OEE")
    if len(param)>1:
        fig,ax1=plt.subplots(len(param),1)
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            temp=k.plot(ax=ax1[i],title=par+" (rolling mean),I={0}".format(interval),marker=marker,**kwargs)
            temp.xaxis.label.set_visible(False)
    else:
        fig,ax1=plt.subplots()
        for i,par in enumerate(param):
            k=g.minor_xs(par).rolling(window=interval).mean()
            k.plot(ax=ax1,title=par+" (rolling mean),I={0}".format(interval),\
                    marker=marker,**kwargs)
    plt.subplots_adjust(hspace=.6)
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
    



