import os
from time import sleep
from act1 import exit as ex

from act1 import closed as cl
from act1 import dark as dk
from act1 import bright as bc

from misc import dead as dead
from misc import color


def strt1():
    print('\n------------------------------------------------------------\n',color.blue, '>>', color.yellow, 'You wake up in a dark cave.', color.blue, '\n  >>', color.yellow, 'You slowly standup and start walking towards a path.\n', color.blue, '>>', color.yellow, 'You see the Excaliber and a shield with the head of medusa \n      lying on the floor\n',
    color.blue, '>>', color.yellow, 'You ignore them and move forward.', 'As you go on you \n      see three chambers...', color.red, '\n\n  [YOU HAVE ENTERED SCENE 1]\n', color.white, '------------------------------------------------------------\n')
def scene1():
    
    print('Choose one of the Pathways you see before you!')
    sleep(1)
    
    print(color.cyan, ' Pathway 1:', color.white,'Exit the cave (uncertain)\n', color.cyan, 'Pathway 2:', color.white,'A Dark pathway where nothing ahead is visible...\n',
    color.cyan, 'Pathway 3:', color.white, 'A mysterious closed door lies ahead...You do not know of anything behind it...\n', color.cyan, 'Pathway 4:', color.white, 'A brightly lit pathway where nothing is visible because of the high brightness...\n', color.red, 'PLEASE CHOOSE YOUR PATHWAY:', color.blue,'(1) | (2) | (3) | (4)', color.white)
    choice1 = input('Choose >> ')
    
    if choice1 == '1':
       print('You chose Path 1!!')
       sleep(1)
       ex.home()
       sleep(1)
       dead.died()
    elif choice1 == '2':
      print('You chose Path 2')
      dk.walk_dark()
      sleep(2)
      dk.cavern_enter()
      sleep(2)
      dk.choice_dark()
    elif choice1 == '3':
      print('You chose Path 3')
      cl.walk_closed()
      sleep(2)
      cl.door_open()
      sleep(2)
      cl.player_choice()
    elif choice1 == '4':
       print('You chose Path 4!!')
       bc.walk()
       sleep(2)
       bc.teleport()
       sleep(2)
       bc.flashback()
    else:
       exit()


       