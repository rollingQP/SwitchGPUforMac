import os
import sys

if len(sys.argv) == 2:
    if 0 <= int(sys.argv[1]) <= 2:
        os.system("sudo pmset -a GPUSwitch " + sys.argv[1])
    else:
        print("Illegal input!")
        print("Usage: chgpu.sh [<command>]")
        print("<command> \n 0:iGPU\n 1:RadeonGPU\n 2:Auto")
        print("Example: type \"python3 chgpu.py 0\" to mandatory use iGPU")
elif len(sys.argv) == 1:
    choose = input("0=iGPU,1=RadeonGPU,2=Auto: ")
    if 0 <= int(choose) <= 2:
        os.system("sudo pmset -a GPUSwitch " + choose)
    else:
        print("Illegal input!")
else:
    print("Too many arguments!")