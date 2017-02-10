import pickle
import datetime
from MineLog.Equipment import Equipment
from MineLog.Equipment import ShiftFile

#takes in Equipment Class and sorts the ActivityData by Date and Shift
def sfsorted(sf_file,shift1=True,shift2=True,shift3=True):
    output = sorted(sf_file,key=lambda x:(datetime.datetime.strptime(x.Date,"%Y-%m-%d"),x.Shift))
    toremove=[]
    for i in output:
        if i.Shift=='1' and not shift1:
            toremove.append(i)
        elif i.Shift=='2' and not shift2:
            toremove.append(i)
        elif i.Shift=='3' and not shift3:
            toremove.append(i)
    for i in toremove:
        del output[output.index(i)]
    return output

#loads file with extention .mlog as Equipment Class
def mload(filepath):
    with open(filepath,'rb') as f:
        return pickle.load(f)
