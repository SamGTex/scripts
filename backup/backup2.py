#! /usr/bin/env python3

import os
import time
import datetime
import argparse
import tkinter as tk
from tkinter import MULTIPLE, filedialog, messagebox
from PIL import ImageTk, Image

from methods.bcolors import bcolors
from methods.add import write
from methods.clean import remove_duplicate
from methods.paths import path

# PARAMETERS
input_path = ''

# fonts
titlefont = ('calibri', 16, 'bold')
labelfont = ('calibri', 12, 'bold')

# get paths
path_obj = path()

# BUTTON FUNCTIONS >>>>>

# update paths from source
def update_source():
    _df = path_obj.df_read
    _name = _df['name'].to_list()
    _path = _df['path'].to_list()

    listbox_source.delete(0, tk.END)
    for i,(name,path) in enumerate(zip(_name,_path)):
        listbox_source.insert(i, f'{name}: {path}')
    return

# update paths from target
def update_target():
    _df = path_obj.df_write
    _name = _df['name'].to_list()
    _path = _df['path'].to_list()

    listbox_target.delete(0, tk.END)
    for i,(name,path) in enumerate(zip(_name,_path)):
        listbox_target.insert(i, f'{name}: {path}')
    return

# get path to source
def choose_path():
    global input_path
    input_path = filedialog.askdirectory()
    lbl_path_folder.configure(text=input_path)

# add path to source
def add_path_source():
    global input_path
    input_name = input_add_name.get()

    # check if name and path 
    if input_path == '' or input_name == '':
        print('Please select a valid name and path!')
        messagebox.showerror("Error", "Please select a valid name and path.")
        return
    
    # add path and check if it works
    if path_obj.add_path_read(input_name, input_path):
        input_path = ''
        input_add_name.delete(0, tk.END)
        lbl_path_folder.configure(text='')
        update_source()
    else:
        messagebox.showerror("Error", "Path already exist.")

# add path to target
def add_path_target():
    global input_path
    input_name = input_add_name.get()

    # check if name and path 
    if input_path == '' or input_name == '':
        print('Please select a valid name and path!')
        messagebox.showerror("Error", "Please select a valid name and path.")
        return
    
    # add path and check if it works
    if path_obj.add_path_write(input_name, input_path):
        input_path = ''
        input_add_name.delete(0, tk.END)
        lbl_path_folder.configure(text='')
        update_target()
    else:
        messagebox.showerror("Error", "Path already exist.")

def del_path_source():
    item_ind = listbox_source.curselection()

    for ind in item_ind:
        name = path_obj.df_read['name'].loc[ind]
        path_obj.del_path_read(name)
        update_source()

def del_path_target():
    item_ind = listbox_target.curselection()

    for ind in item_ind:
        name = path_obj.df_write['name'].loc[ind]
        path_obj.del_path_write(name)
        update_target()

# <<<< BUTTON FUNCTIONS

window = tk.Tk()

#settings
window.geometry('1200x500')
window.title("Texup: Backup Manager")
p1 = ImageTk.PhotoImage(Image.open("images/icon.ico"))
window.tk.call('wm','iconphoto',window._w,p1)

#label source
lbl_add_source_title = tk.Label(window, text='Source', font=titlefont)
lbl_add_source_title.grid(column=0,row=0,columnspan=2,pady=10,sticky=tk.W+tk.S)

#label target
lbl_add_target_title = tk.Label(window, text='Target', font=titlefont)
lbl_add_target_title.grid(column=2,row=0,columnspan=2,pady=10,sticky=tk.W+tk.S)

#show source paths
listbox_source = tk.Listbox(window, width=40, height=20, selectmode=MULTIPLE)
listbox_source.grid(column=0, row=1,columnspan=2,rowspan=3,padx=5,ipadx=5,ipady=1)
update_source()

#show target paths
listbox_target = tk.Listbox(window, width=40, height=20, selectmode=MULTIPLE)
listbox_target.grid(column=2, row=2,columnspan=2,rowspan=3,padx=5,ipadx=5,ipady=1)
update_target()

#delete source path
btn_del_source = tk.Button(window, text='Delete', command=del_path_source, bg='red',font=labelfont, height=1, width=25)
btn_del_source.grid(column=0,row=5,columnspan=2)

#delete target path
btn_del_target = tk.Button(window, text='Delete', command=del_path_target, bg='red',font=labelfont, height=1, width=25)
btn_del_target.grid(column=2,row=5,columnspan=2)

#add source path
btn_add_source_write = tk.Button(window, text='Add', command=add_path_source, bg='#1DB379',font=labelfont, height=1, width=25)
btn_add_source_write.grid(column=0,row=6,columnspan=2)

#add target path
btn_add_target_write = tk.Button(window, text='Add', command=add_path_target, bg='#1DB379',font=labelfont, height=1, width=25)
btn_add_target_write.grid(column=2,row=6,columnspan=2)

#input name
lbl_add_name = tk.Label(window, text='Name', font=labelfont)
lbl_add_name.config()
lbl_add_name.grid(column=0,row=8)

input_add_name = tk.Entry(window, font=labelfont)
input_add_name.grid(column=1, row=8)

#input path
lbl_add_folder = tk.Label(window, text='Folder', font=labelfont)
lbl_add_folder.grid(column=0,row=9)

lbl_path_folder = tk.Label(window, text='', borderwidth=1, relief="solid", height=2, width=30)
lbl_path_folder.grid(column=1,row=9)

btn_add_folder = tk.Button(window, text='Select', command=choose_path, height=1, bg='#09485B',fg='white',font=labelfont)
btn_add_folder.grid(column=2,row=9, sticky=tk.W)

# backup menu


window.mainloop()