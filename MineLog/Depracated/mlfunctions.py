import pandas as pd

#TODO improve this function--too much unnessesary data maninpulation
def GetActivityTime(filepath):
    csvfile = pd.read_csv(filepath)

    start = csvfile['TimeStart'][:-1]
    end = csvfile['TimeStart'][1:]
    timeinterval = pd.Series([en-st for st,en in zip(start,end)])

    activity=csvfile['Activity'][:-1]
    atype= csvfile['Type'][:-1]

    data = pd.DataFrame({'Type':atype,'Activity':activity,'TimeInterval':timeinterval})
    return data

def GetOEE(data):
    totaltime = sum(data['TimeInterval'])
    downtime,idletime = 0,0

    for i in range(len(data)):
        if data.iloc[i].Type == "S":
            idletime += data.iloc[i].TimeInterval
        elif data.iloc[i].Type == "D":
            downtime += data.iloc[i].TimeInterval

    availability = (totaltime-downtime)/totaltime
    utilization = (totaltime-downtime-idletime)/(totaltime-downtime)
    #TODO get efficiency - comes from production time
    efficiency = 1
    #This OEE has the same weights for availability, utilization and efficiency
    oee = availability*utilization*efficiency

    output= {'Availability':availability,
            'Utilization':utilization,
            'Efficiency':1,
            'OEE': oee
            }
    return output

def EvaluateLoggedData(filepath):
    values = GetOEE(GetActivityTime(filepath))
    print(values)

# EvaluateLoggedData('test.csv')

