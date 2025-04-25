from math import *
from random import *

def addDoors():
	picker =  randint(0,1)
	if picker == 1:
		door1,door2,door3 = "premio","vazio","vazio"
	else:
		door1 = "vazio"
		picker = randint(0,1)
		if picker == 1:
		    door2,door3 = "premio","vazio"
		else:
		    door2,door3 = "vazio","premio"
	return [door1,door2,door3]

def openGoatDoor(doors):
    door = ""
        while door != "vazio":
        doorNumber = randint(0,2)
        door = doors[doorNumber]
    return doorNumber
    
def montyhall(doorNumber,switchOk):
    doors = addDoors()
    goatDoor = addDoors()
    while goatDoor == doorNumber:
        goatDoor = openGoatDoor(doors)
    if switchOk == "troca":
        doorNumber = [y for y in range(2) if y not in [doorNumber,goatDoor]]
        return doors[doorNumber[0]]
    else:
        return doors[doorNumber
        
def testMontyHall(playTimes,switch):
    wondragon,wonGoat = 0,0
    for i in range(playTimes):
        prize = montyhall(randint(0,2),switch)
        if prize == "premio":
                wondragon += 1
        else:
                wonGoat += 1
    print "premio:",wondragon
    print "vazio:",wonGoat
    
print('hello world')
'''
testMontyHall(10000,"troca")
testMontyHall(10000,"nao_troca")'''
