#!/usr/bin/python
from random import randint
import locale
from clPeople import getPeopleInt

locale.setlocale( locale.LC_ALL, '' )

playerCash = 15000000

def getCashStr():
    return str(locale.currency(playerCash,grouping=True))

def getCashInt():
    return int(playerCash)

def addCash(Amount):
    global playerCash
    playerCash += Amount

def lowerCash(Amount):
    global playerCash
    playerCash -= Amount

def generateCash():
    global playerCash
    if(randint(0,100)<10):
        playerCash += randint(0,1) * getPeopleInt()
    print(playerCash)


    
