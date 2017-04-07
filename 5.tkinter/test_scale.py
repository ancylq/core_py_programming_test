#!/usr/bin/env python
# coding:utf-8

from Tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

root = Tk()
root.geometry('250x150')

label = Label(root, text='hello world!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(root, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(root,
              text='QUIT',
              command=root.quit,
              activeforeground='white',
              activebackground='red')
quit.pack()

mainloop()