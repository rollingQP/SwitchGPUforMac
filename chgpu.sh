#!/bin/bash
if [ -z "$1" ] 
then
	read -t 10 -p "0=iGPU,1=RadeonGPU,2=Auto: " choose
	if [ $choose -ge 0 -a $choose -le 2 ]
	then
		sudo pmset -a GPUSwitch $choose
	else
		echo "Illegal input!"
	fi
else	
	if [ $1 -ge 0 -a $1 -le 2 ]
	then
		sudo pmset -a GPUSwitch $1
	else
		echo "Illegal input!"
		echo "Usage: chgpu.sh [<command>]"
		echo -e  "<command> \n 0:iGPU\n 1:RadeonGPU\n 2:Auto"
		echo -e "Example: type \"chgpu.sh 0\" to mandatory use iGPU"
	fi
fi
