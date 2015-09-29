#!/usr/bin/python
from random import randint
import locale

locale.setlocale( locale.LC_ALL, '' )

playerCash = 50000

def getCashStr():
    return str(locale.currency(playerCash,grouping=True))

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


    
