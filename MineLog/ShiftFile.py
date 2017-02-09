import pandas as pd
from io import StringIO

class ShiftFile:
    # Attributes:
    #     Equipment,Date,Shift,data
    #     Availability,Utilization,Efficiency,OEE

    def __init__(self,filename):
        self.GetInformation(filename)
        self.Evaluate()

    def GetInformation(self,filename):
        with open(filename,'r') as f:
            x=f.readlines()

        self.Equipment=x[0].replace("\n","").split(":")[1]
        self.Date=x[1].replace("\n","").split(":")[1]
        self.Shift=x[2].replace("\n","").split(":")[1]
        self.data = pd.read_csv(StringIO("".join(x[3:])))

    # Calculates for Availability,Utilization,Efficiency,OEE
    def Evaluate(self):
        atime = self.GetActivityTime()

        totaltime = sum(atime['TimeInterval'])
        downtime,idletime = 0,0

        for i in range(len(atime)):
            if atime.iloc[i].Type == "S":
                idletime += atime.iloc[i].TimeInterval
            elif atime.iloc[i].Type == "D":
                downtime += atime.iloc[i].TimeInterval

        availability = (totaltime-downtime)/totaltime
        utilization = (totaltime-downtime-idletime)/(totaltime-downtime)
        #TODO get efficiency - comes from production time
        efficiency = 1
        #This OEE has the same weights for availability, utilization and efficiency
        oee = availability*utilization*efficiency

        self.Availability = availability
        self.Utilization = utilization
        self.Efficiency = efficiency
        self.OEE = oee

    # Gets activity-time interval from self.data
    def GetActivityTime(self):
        data=self.data
        start = data['TimeStart'][:-1]
        end = data['TimeStart'][1:]
        timeinterval = pd.Series([en-st for st,en in zip(start,end)])

        activity=data['Activity'][:-1]
        atype= data['Type'][:-1]

        activitytime = pd.DataFrame({'Type':atype,'Activity':activity,'TimeInterval':timeinterval})
        return activitytime

# x=ShiftFile('test1.csv')
# print(x.Availability)
# print(x.Utilization)
# print(x.Efficiency)
# print(x.OEE)
# print(x.Equipment)
# print(x.Date)
# print(x.Shift)