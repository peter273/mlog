import shutil
import datetime
import sys
import os
from random import choice 
from random import randrange
def GenerateTestData(Equipment,Date,Shift,activities_no,Type="Shovel"):

    out0 = '"Equipment",'+'"{0}"'.format(str(Equipment))+"\n"
    out0+= '"Type",'+'"{0}"'.format(Type)+"\n"
    out0+= '"Date",'+ '"{0}"'.format(str(Date))+"\n" 

    out0+= '"Shift",'+ '"{0}"'.format(str(Shift))+"\n"

    out=[['"Type"','"Activity"','Time Start','"Operator"']]
    atype = ['"D"']*2
    atype.extend(['"P"']*10)
    atype.extend(['"S"']*5)


    out.append([choice(atype),'"Activity"',0,'"operator"'])
    for i in range(2,activities_no+1):
        out.append([choice(atype),
            '"Activity {0}"'.format(str(i)),
            out[i-1][2]+randrange(6,12),
            '"operator"'])
    out.append(['"E"','"EndShift"',out[-1][2]+randrange(6,28),'"operator"'])

    for i in out:
        i[2] = '"{0}"'.format(i[2])
    out= [map(str,i) for i in out]

    out = [",".join(i) for i in out]
    out = "\n".join(out)

    
    return out0+out


def GenerateCsvs(a,b,c=100,Foldername="datagenerator_output"):
    # c indicates the number of activities in each shiftfile
    original_dir = os.getcwd()
    if c < 20: c=20
    try:
        shutil.rmtree(Foldername)
    except:
        pass
    os.mkdir(Foldername)
    os.chdir(Foldername)
    
    datelist = [datetime.datetime.today()+datetime.timedelta(k) for k in range(b)]
    for i in range(1,a+1):
        for date in datelist:
            for shift in range(1,4):
                if date.month<10:
                    dmonth="0{0}".format(date.month)
                else:
                    dmonth=date.month
                dateoutput="{0}{1}{2}".format(date.year,dmonth,date.day)
                with open("Equipment"+str(i)+"_"+dateoutput+"_Shift"+str(shift)+".txt","w") as f:
                    f.write(GenerateTestData(i,dateoutput,shift,c))

    os.chdir(original_dir)

try:
    GenerateCsvs(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
except Exception as e:
    print(e)
    outmessage='''
    Usage: python3 datagenerator.py a b c
    a = numberofEquipment
    b = numberofdays
    c = number activities
    Total number of files generated = 3*a*b
    '''
    print(outmessage)
