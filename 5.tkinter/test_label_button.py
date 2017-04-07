#!/usr/bin/env python
# coding:utf-8

import Tkinter

root = Tkinter.Tk()
label = Tkinter.Label(root, text='hello world!')
label.pack()

quit = Tkinter.Button(root,
                      text='QUIT',
                      command=root.quit,
                      bg='red',
                      fg='white')
quit.pack(fill=Tkinter.X, expand=1)
Tkinter.mainloop()