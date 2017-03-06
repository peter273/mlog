from MineLog import Equipment,ShiftFile,mload, oeeEquipmentPlot,oeeEquipmentPlot1,param_plot,param_multiple_plot,Moving_AveragePlot
# import numpy as np
# import pandas
# from matplotlib import ticker
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import matplotlib.cbook as cbook
# import datetime
# import os
# import pytz
import time


start = time.time()
# x=Equipment("Equipment1")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save()
# print(len(x.Data))


# x=Equipment("Equipment2")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save()
# print(len(x.Data))

# x=Equipment("Equipment3")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save()
# print(len(x.Data))

y1=mload('Equipment1.mlog')
y1.update()

y2=mload('Equipment2.mlog')
y2.update()

y3=mload('Equipment3.mlog')
y3.update()

#NOTE Plotting Singe Equipment
oeeEquipmentPlot(y1)


chosen_eqlist=[y1,y2,y3]

# NOTE parameter and multiple plotting
#marker options= "o",'.'
#param_plot(chosen_eqlist,'Availability',marker='o')
# param_plot(chosen_eqlist,'Utilization',marker='o')
# param_plot(chosen_eqlist,'OEE',marker='o')
# param_multiple_plot(chosen_eqlist,marker='o')

#NOTE Moving Average
#Moving_AveragePlot(chosen_eqlist,'Availability',interval=2,marker='o')
#Moving_AveragePlot(chosen_eqlist,'Utilization',interval=2,marker='o')
#Moving_AveragePlot(chosen_eqlist,'OEE',interval=2,marker='o')

end= time.time()
print(end-start)
