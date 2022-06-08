#!/usr/bin/python

###################

# Name: Harriet K
# Date : 07/06/2022
#gui examples using tkinter
###################

from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg="purple")
window.geometry("400x400") #fix the window size
f_name = Label(window,text="First Name", font=("Arial",20))
s_name = Label(window,text="Second Name",font=("Arial",20))

f_name.grid(column = 60 , row = 100)
s_name.grid(column=60 , row = 120)

btn = Button(window,text = "Sign Up")
btn.grid(column = 120 , row = 150)

txt_box = Entry(window,width=20)
txt_box.grid(column=100,row =120)
txt_box = Entry(window,width=20)
txt_box.grid(column=100,row =120)


def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg="green")
    msg=Label(top,text= "Welcome to the Pop Up")  font=("Mistral 18"(x=150,y=80))
window.mainloop()
