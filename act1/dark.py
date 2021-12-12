from time import sleep
from misc import color
from act1 import scene as sc
from act1 import closed as cl

def walk_dark():
  print("You cautiously proceed towards the dark cavern..")

def cavern_enter():
  print("You enter the dark cavern, nothing is clearly visible..")
  sleep(2)
  print("You feel your heart racing of fear", color.red)
  sleep(1)
  print("You see someone near you..\n It's the goddess herself, Medusa standing before you...", color.red)
  print("What do think will happen to you now??", color.red)

def choice_dark():
  dark_choice = input(color.white,"Choose the possible outcome:\n 1: You instantly die of petrification\n 2: Nothing happens to you.\n 3: She is dead.\n >> ")
  if dark_choice == '1':
    print("\nYou died of petrification..",color.blue)
    sleep(2)
    print("Returning to beginning", color.blue)
    sleep(2)
    sc.strt1()
  elif dark_choice == '2':
    print("Nothing happens to you", color.blue)
    sleep(2)
    print("You go back outside..")
    sc.scene1()
  elif dark_choice == '3':
    print("You are correct, afterall the Medusa Shield implies that medusa has already been slayed by someone!!") 
    sleep(2)
    print("A second pathway appears before you..")
    sleep(2)
    print("You walk down the new pathway that has opened before you..")
    sleep(1)
    cl.burn()
