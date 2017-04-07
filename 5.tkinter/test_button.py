#!/usr/bin/env python
# coding:utf-8

import Tkinter

root = Tkinter.Tk()
quit = Tkinter.Button(root, text='hello world!', command=root.quit)
quit.pack()
Tkinter.mainloop()