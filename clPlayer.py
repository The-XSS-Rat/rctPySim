#!/usr/bin/python
from random import randint

playerCash = 50000

def getCashStr():
    return str(playerCash)

def getCashInt():
    return int(playerCash)

def addCash(Amount):
    global playerCash
    playerCash += Amount
    print(playerCash)

def lowerCash(Amount):
    global playerCash
    playerCash -= Amount
    print(visitorAmount)


    
