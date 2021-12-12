from time import sleep
from misc import color
from act1 import scene as sc
def back():
  print("you go back to the previous location")
  
def walk_closed():
  print("You slowly walk towards the mysterious closed door..")
  
def door_open():
  print("You try to open the closed door that stands before you..But it won't budge at all. You see a rope and a crowbar lying on the floor. You can also try burning the door down..")
  

def burn():
      print("[NARRATOR]>> A voice speaks to you")
      sleep(1)
      print("[VOICE]>> I'm Knitter the Universal Schemer and You have been chosen Worthy, I will no bestow you the skill of authority ")
      sleep(2)

def player_choice():
  closed_door_choice = input('Please enter your choice of opening the door..\n Burn the Door (1) | rope (2) | crowbar (3):')

  if closed_door_choice == '1':
    print("[NARRATOR]>> You chose to burn the door down...", color.red)
    sleep(1)
    print("You got caught in the fire and died a horrible, painful death!")
    sleep(3)
    print("[NARRATOR]>> You suddenly wake up, to find yourself in room with orb")
    sleep(1)
    burn()

    sleep(3)
  
  elif closed_door_choice == '2':
    print("You chose to use the rope..", color.blue)
    sleep(2)
    
    print("You successfully managed to open the door! Congratulations", color.white)
    sleep(2)
    
    print("You walk into the door, to your surprise you do not find anything there...\n You go back to where you came from to choose some other door..", color.white)
    back()
    sleep(1)
    sc.scene1()

      