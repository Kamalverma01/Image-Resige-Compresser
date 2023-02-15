from tkinter import filedialog

import tkinter as tk

from tkinter import *

from tkinter import ttk

import os

from PIL import ImageTk, Image

from functools import partial

def browseFiles():

    filename = filedialog.askopenfilename(title="Select a Image File",filetypes=[('image files', ('.png', '.jpg'))])



    return filename

def getFolderPath():

    folder_selected = filedialog.askdirectory(title="Select Destination Folder")

    return folder_selected

def submit(a,b,c):

    loc=browseFiles()

    im =Image.open(loc)

    im=im.resize((int(a.get()),int(b.get())))

    saveloc=getFolderPath()

    im.save(saveloc+"/"+c.get()+".jpg")

def Resize():

    roo=tk.Tk()

    roo.geometry("300x100")

    roo.title("Resizer")

    height_var=tk.StringVar()

    width_var=tk.StringVar()

    name_var=tk.StringVar()

    height_label = tk.Label(roo, text = 'Height', font=('calibre',10, 'bold'))

    height_entry = Entry(roo,textvariable = height_var, font=('calibre',10,'normal'))

    width_label = tk.Label(roo, text = 'Width', font = ('calibre',10,'bold'))
    
    width_entry=Entry(roo, textvariable = width_var, font = ('calibre',10,'normal'))

    name_label = tk.Label(roo, text = 'Image Save Name', font = ('calibre',10,'bold'))

    name_entry=Entry(roo, textvariable = name_var, font = ('calibre',10,'normal'))

    dat=partial(submit,height_entry,width_entry,name_entry)

    sub_btn=tk.Button(roo,text = 'Select Image', command = dat)

    height_label.grid(row=0,column=0)

    height_entry.grid(row=0,column=1)

    width_label.grid(row=1,column=0)

    width_entry.grid(row=1,column=1)
    
    name_label.grid(row=2,column=0)

    name_entry.grid(row=2,column=1)

    sub_btn.grid(row=3,column=1)


root = tk.Tk()

root.eval('tk::PlaceWindow . center')

root.title("Image Modifier")

root.geometry('710x100')

root.configure(background='red')

btn1 = Button(root, text = 'Resize', width=100,command = Resize)

btn1.grid(row = 0, column = 1)

btn2 = Button(root, text = 'Compress', width=100, command = None)

btn2.grid(row = 1, column = 1)

btn3 = Button(root, text = 'Combine',  width=100,command = None)

btn3.grid(row = 2, column = 1)

btn4 = Button(root, text = 'Add Text', width=43, command = None)

btn4.grid(row = 3, column = 1)

root.mainloop()