import os
import sys
import pickle
from MineLog.ShiftFile import ShiftFile as sf

def f():
    a=sf('test1.csv')
    with open('test.p','wb') as f:
        pickle.dump(a,f)
