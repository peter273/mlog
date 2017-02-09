from MineLog import Equipment,ShiftFile,mload
import time

start = time.time()
x=Equipment("Equipment1")
x.AddFileDir('/home/coy/MineLog/datagenerator_output')

t1=time.time()
x.save()

t2=time.time()
y=mload('Equipment1.mlog')

t3=time.time()
print("AddFileDir",t1-start)
print("Saving",t2-t1)
print("Loading",t3-t2)






