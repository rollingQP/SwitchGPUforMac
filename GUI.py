import os
import tkinter as tk


def switch_gpu():
    option = var.get()
    try:
        os.system("sudo pmset -a GPUSwitch " + option)
        if option == '0':
            l.config(text="Tried switching to iGPU")
        elif option == '1':
            l.config(text="Tried switching to Radeon GPU")
        else:
            l.config(text="Tried switching to Auto mode")
    except:
        l.config(text="Failed.")


window = tk.Tk()

window.title('Switch GPU for Mac GUI')

# window.geometry('250x100')

# 显示在中间
width = 250
height = 100
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)

var = tk.StringVar()
l = tk.Label(window, width=25, text='请选择')
l.pack(anchor="center")

r1 = tk.Radiobutton(window, text='iGPU', variable=var, value='0', command=switch_gpu, anchor="w")
r1.pack(anchor="w")
r2 = tk.Radiobutton(window, text='Radeon GPU', variable=var, value='1', command=switch_gpu, anchor="w")
r2.pack(anchor="w")
r3 = tk.Radiobutton(window, text='Auto', variable=var, value='2', command=switch_gpu, anchor="w")
r3.pack(anchor="w")

window.mainloop()
