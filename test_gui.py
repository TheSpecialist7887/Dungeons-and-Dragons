import tkinter as tk
from tkinter import *

root= tk.Tk()
canvas= tk.Canvas(root, height=600, width=1000,bg="grey")
canvas.pack()
root.resizable(0,0)

element=["Pyro","Hydro","Cryo","Electro","Geo"]
monster = ["Demogorgon","Mind-Flayer","Giant","Basilisk","Dragon","Owlbear", "Rust monster","Manticore","Wizard","Assassin","Abyss Mage","Titan"]

label1=tk.Label(root, text="Enter your name braveheart: ",bg="grey",font=('castellar',18))
label1.place(x=280,y=220)

def save_name():
    global name
    name=name_entry.get()
    name_entry.destroy()
    label1.destroy()
    N_E.destroy()
    elemnet(name)

def elemnet(name):
    global l1,l2,b1,b2,b3,b4,b5
    wl="Welcome "+name
    l1=tk.Label(root,text=wl,bg="grey",font=('castellar',18))
    l1.place(x=390,y=220)

    l2=tk.Label(root,text="choose your element:",bg="grey",font=('castellar',18))
    l2.place(x=340,y=250)
    
    b1=tk.Button(root, text="PYRO",font=('Serif',11,'bold'),padx=20, pady=7,fg="yellow",bg="#B22222",command=difficulty)
    b1.place(x=250,y=330)
    
    b2=tk.Button(root, text="HYDRO",font=('Serif',11,'bold'), padx=20, pady=7,fg="white",bg="blue",command=difficulty)
    b2.place(x=350,y=330)
    
    b3=tk.Button(root, text="CRYO",font=('Serif',11,'bold'), padx=20, pady=7,fg="#F0F8FF",bg="#5DADE2",command=difficulty)
    b3.place(x=463,y=330)
    
    b4=tk.Button(root, text="ELECTRO",font=('Serif',11,'bold'), padx=20, pady=7,fg="yellow",bg="black",command=difficulty)
    b4.place(x=564,y=330)
    
    b5=tk.Button(root, text="GEO",font=('Serif',11,'bold'), padx=20, pady=7,fg="#FFC300",bg="#6E2C00",command=difficulty)
    b5.place(x=695,y=330)

def difficulty():
    global diff,newbie,hero,titan
    l1.destroy()
    l2.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()

    diff=tk.Label(root,text="CHOOSE YOUR DIFFICULTY LEVEL",bg="grey",font=('castellar',18))
    diff.place(x=280,y=220)

    newbie=tk.Button(root, text="NEWBIE",font=('Serif',11,'bold'), padx=20, pady=7,fg="yellow",bg="green",command=newbie)
    newbie.place(x=280,y=300)

    hero=tk.Button(root, text="HERO",font=('Serif',11,'bold'), padx=20, pady=7,fg="yellow",bg="red",command=hero)
    hero.place(x=463,y=300)

    titan=tk.Button(root, text="TITAN",font=('Serif',11,'bold'), padx=20, pady=7,fg="#D930FD",bg="black",command=titan)
    titan.place(x=634,y=300)



name_entry=tk.Entry(root)
name_entry.configure(font="Arial")
name_entry.focus()
name=name_entry.get()
canvas.create_window(500,300,width=400, height=50, window=name_entry)

N_E=tk.Button(root, text="ENTER",command= save_name)
canvas.create_window(500,390,width=200, height=50, window=N_E)



normalAtk=tk.Button(root, text="Normal Attack", padx=10, pady=5, fg="white", bg="blue")
normalAtk.pack(side="left",padx=10,pady=10)

specialAtk=tk.Button(root, text="Special Attack", padx=10, pady=5, fg="white", bg="red")
specialAtk.pack(side="left",padx=10,pady=10)

flee=tk.Button(root, text="Flee", padx=10, pady=5, fg="white", bg="gray")
flee.pack(side="right",padx=10,pady=10,ipadx=20)

heal=tk.Button(root, text="Heal", padx=10, pady=5, fg="white", bg="green")
heal.pack(side="right",padx=10,pady=10,ipadx=25)

sign=tk.Label(root,text="Developed by Ayan Saha and Divyadeep Mondal \n v1.0.0, 2021", font=("century gothic",11))
sign.pack(side=BOTTOM,expand=True,fill=X)

root.mainloop()
