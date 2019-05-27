#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 21, 2019 03:52:49 PM IST  platform: Windows NT

import sys
import tkinter.messagebox as tm
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("832x579+263+62")
        top.title("Search")
        top.configure(background="#bfeaef")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.272, rely=0.253, relheight=0.431
                , relwidth=0.489)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#CAFAFE")
        self.Frame1.configure(width=395)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.38, rely=0.039, height=31, width=94)
        self.Label1.configure(background="#CAFAFE")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Rockwell} -size 14 -weight bold -slant italic -underline 1")
        self.Label1.configure(foreground="#379683")
        self.Label1.configure(text='''Search''')
        self.Label1.configure(width=94)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.101, rely=0.314, height=21, width=114)
        self.Label2.configure(background="#CAFAFE")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Consolas} -size 12 -weight bold -slant italic")
        self.Label2.configure(foreground="#379683")
        self.Label2.configure(text='''USN:''')
        self.Label2.configure(width=114)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.101, rely=0.549, height=21, width=118)
        self.Label3.configure(background="#CAFAFE")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Consolas} -size 12 -weight bold -slant italic")
        self.Label3.configure(foreground="#379683")
        self.Label3.configure(text='''Address File:''')
        self.Label3.configure(width=118)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.481, rely=0.314,height=20, relwidth=0.441)
        self.Entry1.configure(background="#e0ffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Consolas} -size 10 -slant italic")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=174)

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.481, rely=0.549,height=20, relwidth=0.441)
        self.Entry2.configure(background="#e0ffff")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Consolas} -size 10 -slant italic")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=174)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.38, rely=0.784, height=34, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#6886d8")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {KaiTi} -size 12 -weight bold -slant italic")
        self.Button1.configure(foreground="#0d19a3")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(width=77)
        self.Button1.configure(command=self.clicked)

    def clicked(self):
        usn=self.Entry1.get()
        address=self.Entry2.get()
        if usn=="":
            tm.showerror("Error", "Please enter USN")
        elif address=="":
            tm.showerror("Error", "Please enter address filename")
        else:
            flag = 0
            usn=self.Entry1.get()
            a = int(usn[-3:])
            add = a % 60
            af = open(self.Entry2.get(), 'r')
            line = af.readlines()
            for i in range(0, len(line)):
                if line[add % 60] == '-1':
                    add += 1
                    continue
                else:
                    arr = line[add % 60].strip().split('|')
                    if arr[0] == usn:
                        flag = 1
                        tm.showinfo("Search Info", "Record found")
                        tm.showinfo("Search Information", arr)
                    add += 1
            if flag == 0:
                tm.showerror("Search Error", "Record not found")

if __name__ == '__main__':
    vp_start_gui()





