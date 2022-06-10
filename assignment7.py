#!/usr/bin/python

#Name : Harriet K
#Date 10 / 06 /2022

from tkinter import Tk 
from tkinter import Label
#importing modules
import time 
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S:%p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(master, font=("Calibri",90),bg="black",fg="white")    
clock.pack()

get_time()

master.mainloop()