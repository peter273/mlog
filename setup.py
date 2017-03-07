import sys
from cx_Freeze import setup,Executable

setup(
    name="MineLog",
    version="1.0",
    description = "Mine Equipment Evaluation",
    executables=[Executable("main.py",base="Win32GUI")])
