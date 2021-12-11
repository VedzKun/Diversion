import os
from time import sleep
from act1 import bright_cavern as bc
from act1 import exit as ex
from misc import dead as dead


def strt1():
    print("""\n------------------------------------------------------------\n>> You wake up in a dark cave. 
>> You slowly standup and start walking towards a path. 
>> You see weapons like the sword of arthur 
   and a shield with medusa's broken head lying on the floor
>> You ingore them and move forward, 
   As you go on you see three chambers [YOU HAVE ENTERED SCENE 1] \n 
------------------------------------------------------------\n""")

def scene1():
    print('Choose one of the Pathways you see before you!\n Pathway 1 : The exit of thie cave, you can run back to your home from here...\n Pathway 2: A Dark pathway where nothing ahead is visible...\n Pathway 3: A mysterious clsoed door liea ahead...We do not know of anything behind it...\n Pathway 4 = A brightly lit pathway where nothing is visible because of the high brightness...\n PLEASE CHOOSE YOUR PATHWAY: (1) | (2) | (3) | (4)')

    choice1 = input('Choose >> ')

    if choice1 == '1':
       print('You chose Path 1!!')
       
       ex.return()
       dead.died()
    else:
       exit()