import tkinter as tk
from tkinter import *
import os
import random
import time

root= tk.Tk()
canvas= tk.Canvas(root, height=600, width=1000,bg="grey")
canvas.pack()
root.resizable(0,0)

label1=tk.Label(root, text="Enter your name braveheart: ",bg="grey",font=('old english text mt',18))
#canvas.create_window(500,200,width=400, height=50, window=label1)
label1.place(x=380,y=220)

def save_name():
    global name
    name=name_entry.get()
    name_entry.destroy()
    label1.destroy()
    N_E.destroy()

name_entry=tk.Entry(root)
name_entry.configure(font="century")
name_entry.focus()
name=name_entry.get()
canvas.create_window(500,300,width=400, height=50, window=name_entry)
N_E=tk.Button(root, text="Enter",command= save_name)
canvas.create_window(500,390,width=200, height=50, window=N_E)
normalAtk=tk.Button(root, text="Normal Attack", padx=10, pady=5, fg="white", bg="blue")

normalAtk.pack(side="left",padx=10,pady=10)

specialAtk=tk.Button(root, text="Special Attack", padx=10, pady=5, fg="white", bg="red")

specialAtk.pack(side="left",padx=10,pady=10)

flee=tk.Button(root, text="Flee", padx=10, pady=5, fg="white", bg="gray")

flee.pack(side="right",padx=10,pady=10)

heal=tk.Button(root, text="Heal", padx=10, pady=5, fg="white", bg="green")

heal.pack(side="right",padx=10,pady=10)


root.mainloop()
