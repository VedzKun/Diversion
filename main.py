#!/usr/bin/env python
import os
from time import sleep
from act1 import scene
from misc import color

print(color.purple,"WELCOME USER", color.blue)

sleep(1)
print(' ----------------------------------------------',color.yellow)
print(""" You will be given choices for each scene\n and only choosing the correct option\n will lead to the next scene""",color.blue)
print(' ----------------------------------------------',color.green)
sleep(1)
username = input(' Choose a character name for yourself \n > ')

print(color.white, '\n  | Welcome to Divert - ', username,'\n  | Use your observation skills and level up\n  | through the scenarios in this text-adventure...')

#sleep(3)
print (color.purple, "\n shall we start the game ??")

menuchoice = input(" Yes / No >> ")

if menuchoice == 'yes':
 sleep(1)
 scene.strt1()
 sleep(2)
 scene.scene1()
else:
  exit()   
