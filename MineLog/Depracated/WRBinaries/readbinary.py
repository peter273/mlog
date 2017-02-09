import os
import sys
import pickle
sys.path.append(os.getcwd()+"/../")
from ShiftFile import ShiftFile as sf

with open('test.p','rb') as f:
    x=pickle.load(f)
print(x.Equipment)
