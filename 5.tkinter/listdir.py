#!/usr/bin/env python
# coding:utf-8

import os
from time import sleep
from Tkinter import *

class DirList(object):
    
    def __init__(self, initdir=None):
        self.root = Tk()
        self.label = Label(self.root, text='Directory Lister v1.1')
        self.label.pack()
        
        self.cwd = StringVar(self.root)
        self.dirl = Label(self.root, fg='blue', 
                          font=('Helvetica', 12, 'bold'))
        self.dirl.pack()
        
        self.dirfm = Frame(self.root)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50,
                            yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()
        
        self.dirn = Entry(self.root, width=50, textvariable=self.cwd)
        
        
        self.bfm = Frame(self.root)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                          activeforeground='white',
                          activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory',
                         command=self.doLS,
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='QUIT',
                           command=self.root.quit,
                           activeforeground='white',
                           activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()
        
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()
            
    def clrDir(self, ev=None):
        self.cwd.set('')
        
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()
        
    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir
        
        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'
            
        if error:
            self.cwd.set(error)
            self.root.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.root.update()
            return
        
        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.root.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')
        
def main():
    d = DirList(os.curdir)
    mainloop()
    
if __name__ == '__main__':
    main()
        