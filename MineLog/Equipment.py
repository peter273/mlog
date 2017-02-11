import pickle
import os
import pandas
import datetime
from os.path import join,isfile,basename
from MineLog.ShiftFile import ShiftFile

#loads file with extention .mlog as Equipment Class
def mload(filepath):
    with open(filepath,'rb') as f:
        return pickle.load(f)

class dcont:
    def __init__(self,timedata):
        self.timedata=timedata
class Equipment:
    # Attributes:
    #     Name,Type, ActivityData

    def __init__(self,Name="Equipment1",Type="Type"):
        self.Name = Name
        self.Type = Type
        self.Data = pandas.DataFrame()

    def AddFileFromDirectory(self,filedir):
        files=(f for f in  os.listdir(filedir) if isfile(join(filedir,f)))
        for f in files:
            try:
                self.AddFile(join(filedir,f))
            except Exception as e:
                print("Error in adding File:",f)
                print(e)

    def AddFile(self,SF):
        if basename(SF).split("_")[0]==self.Name and isfile(SF):
            sf = ShiftFile(SF)
            self.AddData(sf)

    #TODO set the default saving directory
    def save(self,filepath=os.getcwd()):
        with open(filepath+"/"+self.Name+".mlog",'wb') as f:
            pickle.dump(self,f)
    def update(self):
        self.Data = self.Data.sort_values(by=["Shift","Date"]).reset_index(drop=True)
    def saveas(self,Name,filepath=os.getcwd()):
        self.Name=Name
        self.save(filepath)

    def AddData(self,shiftfile):
        attributes = set(shiftfile.__dict__.keys()) - set(['Equipment'])
        a={i:[] for i in attributes}

        for attrb in attributes:
            # if attrb == 'data':
            #     a[attrb].append(dcont(getattr(shiftfile,attrb)))
            # else:
            a[attrb].append(getattr(shiftfile,attrb))
        self.Data = self.Data.append(pandas.DataFrame.from_dict(a))

    # # TODO improve the RemoveFile function
    # def RemoveFile(self,Equipment,Date,Shift):
    #     index=None
    #     for i in self.ActivityData:
    #         if i.Equipment == Equipment and i.Date == Date and i.Shift == Shift:
    #             index=self.ActivityData.index(i)
    #             break
    #     try:
    #         del self.ActivityData[index]
    #     except Exception as e:
    #         pass
