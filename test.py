from MineLog import Equipment,ShiftFile,mload, \
    oeeEquipmentPlot,Moving_AveragePlot
# import numpy as np
# import pandas
# from matplotlib import ticker
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import matplotlib.cbook as cbook
# import datetime
import os
# import pytz

import time
import matplotlib
from matplotlib import pyplot as plt

equipment_file_location=os.path.join(os.getcwd(),'Equipment')

start = time.time()
# for i in range(1,16):
#     x=Equipment("Equipment{0}".format(i))
#     x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
#     x.update()
#     x.save(equipment_file_location)
# print(len(x.Data))


# x=Equipment("Equipment1")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save(equipment_file_location)
# print(len(x.Data))


# x.data.iloc[1]
# x=Equipment("Equipment3")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save(equipment_file_location)
# print(len(x.Data))

# y1=mload(os.path.join(equipment_file_location,'Equipment1.mlog'))
# y1.update()

# y2=mload(os.path.join(equipment_file_location,'Equipment2.mlog'))
# y2.update()

Ei=lambda i:'Equipment{0}'.format(i)
for i in range(1,5):
    x=Equipment(Ei(i))
    x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
    x.update()
    x.save(equipment_file_location)

# y3=mload(os.path.join(equipment_file_location,'Equipment1.mlog'))
# y3.update()

# y4=mload(os.path.join(equipment_file_location,'Equipment2.mlog'))
# y4.update()
#month
# returns (year,month)
# print(b.iloc[1].name)
# print(Moving_AveragePlot([y3,y4],['Utilization','Availability'],interval=2,export_data=True))
# plt.show()

# #NOTE Plotting Singe Equipment
# # oeeEquipmentPlot(y1)


# chosen_eqlist=[y1,y2,y3]
 

# # NOTE parameter and multiple plotting
# #marker options= "o",'.'
# # param_plot(chosen_eqlist,'Availability',marker='o')
# # param_plot(chosen_eqlist,'Utilization',marker='o')
# # param_plot(chosen_eqlist,'OEE',marker='o')
# # param_multiple_plot(chosen_eqlist,marker='o')


# #NOTE Moving Average
# parameter=["Availability"]
# Moving_AveragePlot(chosen_eqlist,['Availability','Utilization',"OEE"],interval=0,marker='o')
# # Moving_AveragePlot(chosen_eqlist,'Utilization',interval=4,marker='o')
# # Moving_AveragePlot(chosen_eqlist,'OEE',interval=2,marker='o')

# end= time.time()
# print(end-start)
