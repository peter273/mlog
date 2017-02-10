import pickle
import os
from os.path import join,isfile
from MineLog.ShiftFile import ShiftFile
import datetime

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

class Equipment:
    # Attributes:
    #     Name,Type, ActivityData

    def __init__(self,Name="Equipment1",Type="Type"):
        self.Name = Name
        self.Type = Type
        self.ActivityData = []
    def __str__(self):
        return str({"Name": self.Name,
                "Type": self.Type,
                })
    def AddFileDir(self,filedir):
        files=[f for f in  os.listdir(filedir) if isfile(join(filedir,f))]
        for f in files:
            try:
                if f.split("_")[0] == self.Name:
                    self.AddFile(join(filedir,f))
            except Exception as e:
                print("Error in adding File:",f)
                print(e)
    def AddFile(self,SF):
        sf = ShiftFile(SF)
        self.ActivityData.append(sf)

    # TODO improve the RemoveFile function
    def RemoveFile(self,Equipment,Date,Shift):
        index=None
        for i in self.ActivityData:
            if i.Equipment == Equipment and i.Date == Date and i.Shift == Shift:
                index=self.ActivityData.index(i)
                break
        try:
            del self.ActivityData[index]
        except Exception as e:
            pass

    #TODO set the default saving directory
    def save(self,filepath=os.getcwd()):
        with open(filepath+"/"+self.Name+".mlog",'wb') as f:
            pickle.dump(self,f)
    def saveas(self,Name,filepath=os.getcwd()):
        self.Name=Name
        self.save(filepath)


