#! /usr/bin/env python3

import os
import time
import datetime
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

from methods.bcolors import bcolors
from methods.add import write
from methods.clean import remove_duplicate
from methods.paths import path

# PARAMETERS
input_path_source = ''

# fonts
titlefont = ('calibri', 16, 'bold')
labelfont = ('calibri', 12, 'bold')

# get paths
path_obj = path()

# BUTTON FUNCTIONS >>>>>
def choose_path_source():
    global input_path_source
    input_path_source = filedialog.askdirectory()
    btn_add_source_folder.configure(text='Change Folder')
    lbl_add_source_folder.configure(text=input_path_source)



def add_path_source():
    global input_path_source
    input_name = input_add_source_name.get()

    # check if name and path 
    if input_path_source == '' or input_name == '':
        print('Please select a valid name and path!')
        messagebox.showerror("Error", "Please select a valid name and path.")
        return
    
    # add path and check if it works
    if path_obj.add_path_read(input_name, input_path_source):
        input_path_source = ''
        input_add_source_name.delete(0, tk.END)
        btn_add_source_folder.configure(text='Select Folder')
        lbl_add_source_folder.configure(text='Please select a folder!')
    else:
        messagebox.showerror("Error", "Path already exist.")

# <<<< BUTTON FUNCTIONS

window = tk.Tk()

# settings
window.geometry('800x500')
window.title("Texup: Backup Manager")
p1 = ImageTk.PhotoImage(Image.open("images/icon.ico"))
window.tk.call('wm','iconphoto',window._w,p1)

# add SOURCE path >>>
lbl_add_source_title = tk.Label(window, text='Define name and choose path to source directory.', font=titlefont)
lbl_add_source_title.grid(column=0,row=0, columnspan=3,pady=10,sticky=tk.W+tk.S)

#select name
lbl_add_source_name = tk.Label(window, text='Name', font=labelfont)
lbl_add_source_name.config()
lbl_add_source_name.grid(column=0,row=1, ipady=5, pady=5, padx=5, sticky=tk.S+tk.W)

input_add_source_name = tk.Entry(window, font=labelfont)
input_add_source_name.grid(column=0, row=2, ipady=5, pady=5, padx=5)

#select path
btn_add_source_folder = tk.Button(window, text='Select Folder', command=choose_path_source, height=1, width=14, bg='#09485B',fg='white',font=labelfont)
btn_add_source_folder.grid(column=1,row=1,padx=5,sticky=tk.W+tk.S)

lbl_add_source_folder = tk.Label(window, text='Please select a folder!', borderwidth=1, relief="solid", height=2, width=40)
lbl_add_source_folder.grid(column=1,row=2,padx=5,ipadx=5,ipady=1)

#write path to csv
lbl_add_source_write = tk.Button(window, text='Add', command=add_path_source, bg='#1DB379',font=labelfont, height=1, width=4)
lbl_add_source_write.grid(column=2, row=2, ipadx=0, ipady=2, sticky=tk.E)
# <<<


window.mainloop()
