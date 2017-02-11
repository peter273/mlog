from MineLog import Equipment,ShiftFile,mload
import matplotlib.pyplot as plt
import os
import time


start = time.time()
# x=Equipment("Equipment1")
# x.AddFileFromDirectory(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))
# x.update()
# x.save()

y=mload('Equipment1.mlog')
end= time.time()
print(end-start)

print(y.Data)
end= time.time()
print(end-start)
# print(y.Data.data.iloc[0])

# print(list(map(str,sfdata.Shift)))
# print(sfdata['Availability'])
# ax=sfdata["Availability"].plot(kind='bar',alpha=0.5)
# label = [i.strftime("%b %d,%y")+" S"+str(j) for i,j in zip(sfdata.Date,sfdata.Shift)]

# ax.set_xticklabels(label,rotation=20)
# plt.show()

# print(type(sfdata.iloc[0].Date))
# plt.plot(sf.iloc[0]
# sfdata.plot.scatter(x='Date',y='Utilization')
# plt.show()








