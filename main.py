#!/usr/bin/env python
import os
from time import sleep
from act1 import scene
     
sleep(2)
print('----------------------------------------------')
print("""You will be given choices for each scene and only choosing the correct option will lead to the next scene""")
print('----------------------------------------------')
username = input('Choose a character name for yourself \n > ' )

print('Welcome to Divert,', username, '. Use your observation skills and level up through the scenarios in this thrilling adventure...')

#sleep(3)
print ("shall we start the game ??")

menuchoice = input('yes/no >> ')

if menuchoice == 'yes':
 sleep(1)
 scene.strt1()
 sleep(1)
 scene.scene1()
else:
  exit()   
