from MineLog import Equipment,ShiftFile,mload
import os
import time


start = time.time()
x=Equipment("Equipment")
x.AddFileDir(os.path.join(os.getcwd(),'MineLog/datagenerator_output'))

t1=time.time()
x.save()


t2=time.time()
t7=time.time()
y=mload('Equipment.mlog')

t3=time.time()
print("AddFileDir",t1-start)
print("Saving",t2-t1)
print("Loading",t3-t2)






