import time
import random
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter.messagebox import showerror


root= tk.Tk()
canvas= tk.Canvas(root, height=600, width=1000,bg="#264c5e")
canvas.pack()
root.resizable(0,0)
btn=tkFont.Font(family="Castellar", size=18,weight=tkFont.BOLD)
stats=tkFont.Font(family="old english text mt", size=18)

n_atk=15
s_atk=35
hero_hp=100
monster_hp=100

element=["Pyro","Hydro","Cryo","Electro","Geo"]
monster = ["Demogorgon","Mind-Flayer","Giant","Basilisk","Dragon","Owlbear", "Rust monster","Manticore","Wizard","Assassin","Abyss Mage","Titan"]

m_element=random.choice(element)
random.shuffle(monster)
spawn_monster = m_element+" "+random.choice(monster)

label1=tk.Label(root, text="Enter your name braveheart: ",bg="#264c5e",fg='white',font=btn,bd=5)
label1.place(x=270,y=220)

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
    l1=tk.Label(root,text=wl,bg="#264c5e",fg='white',font=btn)
    l1.place(x=390,y=220)

    l2=tk.Label(root,text="choose your element:",bg="#264c5e",fg='white',font=btn)
    l2.place(x=340,y=250)
    
    b1=tk.Button(root, text="PYRO",font=('Serif',11,'bold'),padx=20, pady=7,fg="yellow",bg="#B22222",command=lambda: difficulty("pyro"))
    b1.place(x=250,y=330)
    
    b2=tk.Button(root, text="HYDRO",font=('Serif',11,'bold'), padx=20, pady=7,fg="white",bg="blue",command=lambda: difficulty("hydro"))
    b2.place(x=350,y=330)
    
    b3=tk.Button(root, text="CRYO",font=('Serif',11,'bold'), padx=20, pady=7,fg="#F0F8FF",bg="#5DADE2",command=lambda: difficulty("cryo"))
    b3.place(x=463,y=330)
    
    b4=tk.Button(root, text="ELECTRO",font=('Serif',11,'bold'), padx=20, pady=7,fg="yellow",bg="black",command=lambda: difficulty("electro"))
    b4.place(x=564,y=330)
    
    b5=tk.Button(root, text="GEO",font=('Serif',11,'bold'), padx=20, pady=7,fg="#FFC300",bg="#6E2C00",command=lambda: difficulty("geo"))
    b5.place(x=695,y=330)


def difficulty(ele):
    global diff_title,newbie,hero,titan,hero_element
    hero_element=ele
    l1.destroy()
    l2.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()

    diff_title=tk.Label(root,text="CHOOSE YOUR DIFFICULTY LEVEL",bg="#264c5e",fg='white',font=btn)
    diff_title.place(x=280,y=220)

    newbie=tk.Button(root, text="NEWBIE",font=('Serif',11,'bold'),command=lambda:gameplay("newbie"),padx=20, pady=7,fg="white",bg="green")
    newbie.place(x=280,y=300)

    hero=tk.Button(root, text="HERO",font=('Serif',11,'bold'),command=lambda:gameplay("hero"), padx=20, pady=7,fg="yellow",bg="red")
    hero.place(x=463,y=300)

    titan=tk.Button(root, text="TITAN",font=('Serif',11,'bold'),command=lambda:gameplay("titan"), padx=20, pady=7,fg="#D930FD",bg="black")
    titan.place(x=634,y=300)


def gameplay(diff):
    global n_atk,s_atk,heal

    newbie.destroy()
    hero.destroy()
    titan.destroy()
    diff_title.destroy()

    if(diff=="newbie"):
        heal=3
    elif(diff=="hero"):
        n_atk-=2
        s_atk-=3
        heal=1
    elif(diff=="titan"):
        n_atk-=3
        s_atk-=5
        heal=0

    if(m_element==hero_element):
        n_atk-=3
        s_atk-=5
    else:
        n_atk+=2
        s_atk+=3
    game_entry()






def normal_atk():
    global monster_hp,hero_hp,n_atk,monster_status,hero_status
    monster_hp-=n_atk
    monster_status.destroy()
    hero_status.destroy()
    attack_value = random.randint(1,3)

    if attack_value == 1:
        hero_hp-=10
    elif attack_value == 2:
        hero_hp-=15
    elif attack_value==3:
        hero_hp-=20
    game_entry()

def special_atk():
    global monster_hp,hero_hp,s_atk,monster_status,hero_status
    monster_status.destroy()
    hero_status.destroy()

    chance=random.randint(1,10)
    
    if chance%2==0:
        monster_hp-=s_atk
    elif chance%2==1:
        monster_hp-=0
    attack_value = random.randint(1,3)

    if attack_value == 1:
        hero_hp-=10
    elif attack_value == 2:
        hero_hp-=15
    elif attack_value==3:
        hero_hp-=20
    game_entry()

def heal():
    global hero_hp,hero_status,heal
    if heal>0:
        hero_hp+=30
        heal-=1
        game_entry()

    else:
        showerror("Error", message="You are out of potions!")
        game_entry()

def flee():
    hero_status.destroy()
    fled=tk.Label(root,text="ran away",bg="white",font=stats)
    fled.place(x=700,y=100)
    f=Label(root,text="You fled like a coward......\n You have no honour.......",font=btn,bg="grey")
    f.place(x=300,y=300)
    normalAtk.config(state=DISABLED)
    specialAtk.config(state=DISABLED)
    heal_bt.config(state=DISABLED)
    flee_bt.config(state=DISABLED)


def game_entry():
    global hero_hp,monster_hp,name,heal
    global monster_status,hero_status
    normalAtk.config(state=NORMAL,fg="white",bg="#E01C29",relief=RAISED,bd=10)
    specialAtk.config(state=NORMAL,fg="white",bg="#5E367F",relief=RAISED,bd=10)
    heal_bt.config(state=NORMAL,fg="white",bg="green",relief=RAISED,bd=10)
    flee_bt.config(state=NORMAL,fg="black",bg="grey",relief=RAISED,bd=10)
    if hero_hp>=1:
        hero_name=tk.Label(root,text=name+" ("+hero_element+")",fg="#ff9912",bg="#264c5e",font=btn)
        hero_name.place(x=100,y=100)
        hero_status=tk.Label(root,text=hero_hp,bg="white",font=stats)
        hero_status.place(x=700,y=100)

        monster_name=tk.Label(root,text=spawn_monster,fg="#b0bf1a",bg="#264c5e",font=btn)
        monster_name.place(x=100,y=150)
        monster_status=tk.Label(root,text=monster_hp,bg="white",font=stats)
        monster_status.place(x=700,y=150)

        potion=tk.Label(root,text="Potions Available",fg="#7DF9FF",bg="#264c5e",font=btn)
        potion.place(x=100,y=200)
        potion_count=tk.Label(root,text=heal,bg="white",font=stats)
        potion_count.place(x=700,y=200)


        if monster_hp<1:
            w=Label(root,text="You Win!!",font=btn,bg="#264c5e")
            w.place(x=300,y=300)
            normalAtk.config(state=DISABLED)
            specialAtk.config(state=DISABLED)
            heal_bt.config(state=DISABLED)
            flee_bt.config(state=DISABLED)

    elif hero_hp<1:
            hero_name=tk.Label(root,text=name+" ("+hero_element+")",bg="#264c5e",font=btn)
            hero_name.place(x=100,y=150)
            hero_status=tk.Label(root,text=hero_hp,bg="white",font=stats)
            hero_status.place(x=700,y=150)
            monster_name=tk.Label(root,text=spawn_monster,bg="grey",font=btn)
            monster_name.place(x=100,y=200)
            monster_status=tk.Label(root,text=monster_hp,bg="white",font=stats)
            monster_status.place(x=700,y=200)
            potion=tk.Label(root,text="potion",bg="grey",font=btn)
            potion.place(x=100,y=500)
            potion_count=tk.Label(root,text=heal,bg="white",font=stats)
            potion_count.place(x=700,y=500)
            l=Label(root,text="You Lost.....",font=btn,bg="grey")
            l.place(x=300,y=300)
            normalAtk.config(state=DISABLED)
            specialAtk.config(state=DISABLED)
            heal_bt.config(state=DISABLED)
            flee_bt.config(state=DISABLED)



name_entry=tk.Entry(root,bd=5)
name_entry.configure(font="Arial")
name_entry.focus()
name=name_entry.get()
canvas.create_window(500,300,width=400, height=50, window=name_entry)

N_E=tk.Button(root, text="ENTER REALM",command=save_name,bg='#B1171C',fg='white')
canvas.create_window(500,390,width=200, height=50, window=N_E)




normalAtk=tk.Button(root, text="Normal Attack", padx=10, pady=5,relief=SUNKEN,command=normal_atk,state=DISABLED)
normalAtk.pack(side="left",padx=10,pady=10)

specialAtk=tk.Button(root, text="Special Attack", padx=10, pady=5,relief=SUNKEN,command=special_atk,state=DISABLED)
specialAtk.pack(side="left",padx=10,pady=10)

flee_bt=tk.Button(root, text="Flee", padx=10, pady=5,relief=SUNKEN, command=flee,state=DISABLED)
flee_bt.pack(side="right",padx=10,pady=10,ipadx=20)

heal_bt=tk.Button(root, text="Heal", padx=10, pady=5,relief=SUNKEN, command=heal,state=DISABLED)
heal_bt.pack(side="right",padx=10,pady=10,ipadx=25)

sign=tk.Label(root,text="Developed by Ayan Saha and Divyadeep Mondal \n v1.0.0, 2021", font=("century gothic",11))
sign.pack(side=BOTTOM,expand=True,fill=X)

root.mainloop()
