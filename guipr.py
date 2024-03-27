# GUI programming - python

#importing packeg or module
import tkinter as tk
from tkinter import *

#creating window
window=tk.Tk()

#creating title and its size
window.title("Anil Eranna")
window.geometry("400x300")

#creating heading
heading=Label(window,text="Login page",font="sans 16 bold",bg="green",fg="yellow").pack(fill="both")
#Creating first label and entry box
l1=Label(window,text="User name:").pack()
e1=Entry(window).pack()

#creating second label and entry box
l2=Label(window,text="password:").pack()
e2=Entry(window,show=("*")).pack()
#creating button
b1=Button(window,text="Submit").pack()

#mainloop
window.mainloop()
