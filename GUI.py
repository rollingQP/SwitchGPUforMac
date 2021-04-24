import os
import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('250x100')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(window, width=25, text='请选择')
l.pack(anchor ="center")


# 第6步，定义选项触发函数功能
def switch_gpu():
    option = var.get()
    os.system("sudo pmset -a GPUSwitch " + option)
    if option == '0':
        l.config(text="Switch to iGPU success")
    elif option == '1':
        l.config(text="Switch to Radeon GPU success")
    else:
        l.config(text="Switch to Auto mode success")


# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='iGPU', variable=var, value='0', command=switch_gpu,anchor ="w")
# r1.grid(row=1, column=1)
r1.pack(anchor ="w")
r2 = tk.Radiobutton(window, text='Radeon GPU', variable=var, value='1', command=switch_gpu, anchor ="w")
# r2.grid(row=2, column=1)
r2.pack(anchor ="w")
r3 = tk.Radiobutton(window, text='Auto', variable=var, value='2', command=switch_gpu, anchor ="w")
# r3.grid(row=3, column=1)
r3.pack(anchor ="w")

# 第7步，主窗口循环显示
window.mainloop()