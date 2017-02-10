import pickle
import os
from os.path import join,isfile
from MineLog.ShiftFile import ShiftFile
import datetime


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


