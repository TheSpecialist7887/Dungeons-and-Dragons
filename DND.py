import random
import time

print("Welcome to Dungeons and Dragons pocket edition")
print("Developed by Ayan Saha & Divyadeep Mondal")

name = input("What is your name braveheart?\n>>>")

p_element_choice=int(input("Choose The Hero's element\n 1)Pyro\n 2)Hydro\n 3)Cryo\n 4)Electro\n 5)Geo\n>>>"))
element=["Pyro","Hydro","Cryo","Electro","Geo"]
p_element=element[p_element_choice-1]

m_element=random.choice(element)

monster = ["Demogorgon","Mind-Flayer","Giant","Basilisk","Dragon","Owlbear", "Rust monster","Manticore","Wizard","Assassin","Abyss Mage","Titan"]
random.shuffle(monster)
spawn_monster = m_element+" "+random.choice(monster)
p_health = 100
m_health = 100
normal_attack_dmg=15
special_attack_dmg=35

diffic=int(input("\n Choose Difficulty:\n[1]Normal\n[2]Difficult\n[3]Nightmare Mode\n >>> "))

if(diffic==1):
  Health_potion=3
  print("\n {} has".format(name),Health_potion,"Health Potions. Use them wisely.")
elif(diffic==2):
  Health_potion=1
  normal_attack_dmg-=2
  special_attack_dmg-=3
  print("\n {} is already tired".format(name),"Use your strength wisely")
  print("\n {} has 1 Health Potion Left.".format(name),"\n Exhaustion reduced normal attack damage by 2HP\n Special attack damage reduced by 3HP")
elif(diffic==3):
  Health_potion=0
  normal_attack_dmg-=3
  special_attack_dmg-=4
  print("\n {} has been bamboozled and sedated".format(name))
  print("\n {} has no health potions left".format(name),"\n Daze reduced normal attack damage by 3HP\n Special attack damage reduced by 4 HP")
else:
  print("\nWrong Choice. Try again")
  diffic=int(input("\n Choose Difficulty:\n[1]Normal\n[2]Difficult\n[3]Nightmare Mode\n >>> "))


print(" ")
print("a {} appeared!".format(spawn_monster))
print(" ")


if(p_element==m_element):
    normal_attack_dmg=normal_attack_dmg-5
    special_attack_dmg=special_attack_dmg-10
else:
    normal_attack_dmg=normal_attack_dmg+2
    special_attack_dmg=special_attack_dmg+5

while p_health > 1:
  time.sleep(1)
  print("==================")
  print(" ")
  print("{}'s life: {} HP\n{}'s life: {} HP".format(name, p_health, spawn_monster, m_health))
  print(" ")
  time.sleep(1)
  print("What {} will do?".format(name))
  attack = int(input("[1] Normal attack\n[2] Special attack\n[3] Recover life\n[4] Flee\n>>>"))
  print(" ")
  if(attack>4 or attack<1):
      attack=int(input("Wrong choice. Try again.\n>>> "))

  if attack == 1:
    time.sleep(1)
    print("{} dealt".format(name),normal_attack_dmg, "damage!")
    m_health = m_health - normal_attack_dmg
    time.sleep(1)
    print("{} has {} HP now!".format(spawn_monster, m_health))
    print(" ")

  elif attack == 2:
    time.sleep(1)
    chance = random.randint(1,2)

    if chance == 1:
      print("{} dealt".format(name),special_attack_dmg, "damage!")
      m_health = m_health - special_attack_dmg
      time.sleep(1)
      print("{} has {} HP now!".format(spawn_monster, m_health))
      print(" ")

    else:
      print("{} failed!".format(name))

  elif attack == 3:
    if(Health_potion>0):
      time.sleep(1)
      print("{} recovered 30 HP!".format(name))
      time.sleep(1)
      p_health = p_health + 30
      Health_potion-=1
      print("\nHealth potions left: ",Health_potion)
      print("\n{} has {} HP now!".format(name, p_health))
    else:
      print("No Potions left. Move invalid.")
  elif attack == 4:
    time.sleep(1)
    print("{} fled like a coward.....".format(name))
    time.sleep(1)
    print("{} has no honor".format(name))
    break


  if p_health < 1:
    time.sleep(1)
    print("{} lost...".format(name))
    time.sleep(2)
    break

  elif m_health < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break


  print("==================")
  print(" ")
  print("{} Attacks!".format(spawn_monster))
  time.sleep(2)
  print(" ")

  attack_value = random.randint(1,3)

  if attack_value == 1:
    print("{} dealt 10 damage!".format(spawn_monster))
    p_health = p_health - 10
    time.sleep(1)
    print("{} has {} HP now!".format(name, p_health))
    print(" ")

  elif attack_value == 2:
    print("{} dealt 15 damage!".format(spawn_monster))
    p_health = p_health - 15
    time.sleep(1)
    print("{} has {} HP now!".format(name, p_health))
    print(" ")

  elif attack_value == 3:
    print("{} dealt 20 damage!".format(spawn_monster))
    p_health = p_health - 20
    time.sleep(1)
    print("{} has {} HP now!".format(name, p_health))
    print(" ")

  print(" ")


  if p_health < 1:
    time.sleep(1)
    print("{} lost...".format(name))
    time.sleep(2)
    break

  elif m_health < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break

input("Press Enter key to exit")