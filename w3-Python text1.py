# -*- coding: utf-8 -*-

import tkinter as tk
#import tkinter.ttk
#import unittest
#import serial
import threading
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
import time
import os

def show1():
    i = 0
    # 建立一個子執行緒
    t = threading.Thread(target=showMessage, args=())
    # 執行該子執行緒
    t.start()
    while i <= 10:
        print(i)
        time.sleep(1)
        i += 1



def showMessage():
    top = tk.Toplevel()
    l = tk.Label(top, text='進度', width=20)
    l.pack()

    def show():
        for i in range(100):
            # 每次加一
            progressbarOne['value'] = i + 10
            # 更新畫面
            top.update()
            time.sleep(0.05)

    progressbarOne = ttk.Progressbar(top)
    progressbarOne.pack(pady=20)
    # 進度值最大值
    progressbarOne['maximum'] = 100
    # 進度值初始值
    progressbarOne['value'] = 0
    show()
    top.destroy()
    top.mainloop()



root = tk.Tk()
b1 = tk.Button(root, text='start1', command=show1)
b1.pack()
root.mainloop()