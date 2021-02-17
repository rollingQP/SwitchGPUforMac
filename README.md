# SwitchGPUforMac
A bash script that can switch GPU types on Mac

----

## Introduction
The main idea of the script is using `sudo pmset -a GPUSwitch` to switch GPU of your Mac.

It's only been tested on MacBook Pro (16 inches，2019).

You can just run `./chgpu` or configure the environment variables for it.

Don't forget to run `chmod +x chgpu` before if you have not.

----

## Usage
```
chgpu [<args>]
  args  0=iGPU,1=RadeonGPU,2=Auto
```
