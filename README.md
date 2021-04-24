# SwitchGPUforMac
A bash script that can switch GPU types on Mac

----
## Attention 注意
.app文件还未签名，因此可能要自行编译才能用在自己的mac上。编译方法稍后附上。

## Introduction
The main idea of the script is using `sudo pmset -a GPUSwitch` to switch GPU of your Mac.

It's only been tested on MacBook Pro (16 inches，2019).

There are four ways to use the program.

### Shell Script

You can just run `./chgpu.sh` or configure the environment variables for it.

Don't forget to run `chmod +x chgpu.sh` before if you have not.

### Python Script

You can run `python3 chgpu.py` if you have installed Python 3. Note that Python 2 is not supported.

### Binary file

You can download and run the binary file `chgpu`. In general, you can double-click it to run it. It may take a while to load.

### GUI binary file

You can download and double click to run the app `Switch GPU for Mac.app`. If it doesn't work, right click it and then run. It's very intuitive, so I don't think you need a tutorial.

----

## Usage
```
chgpu [<args>]
  args  0=iGPU,1=RadeonGPU,2=Auto
```
