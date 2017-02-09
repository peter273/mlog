import os
import shutil
from itertools import product
from os import walk,listdir
from os.path import isfile,join

def FileCreate(path,Items=4):
    File_Name=["File"+str(i)+"_"+str(j) for i,j in product(range(1,Items),repeat=2)]
    original_dir=os.getcwd()
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)

    for filename in File_Name:
        with open(filename+".csv","+a") as f:
            pass
    os.chdir(original_dir)

def FileSorter(cwd,foldername,SortedFolderName=""):
    f=[]
    for (dirpath,dirnames,filenames) in walk(join(cwd,foldername)):
        f.extend(filenames)
    print(f)

# FileSorter(os.getcwd(),"folder")
FileCreate(join(os.getcwd(),"folder"))

