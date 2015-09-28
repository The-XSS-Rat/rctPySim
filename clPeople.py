#!/usr/bin/python
from random import randint

visitorAmount = 0
minAmount = 500
maxAmount = 80

chanceOfPlus = 70

def generatePeople():
    global chanceOfPlus
    global chanceOfMinus
    global visitorAmount

    chancePlusMinus = randint(0,100)
    
    if(randint(0,1000) < 5):
        if chancePlusMinus >= (100 - chanceOfPlus) and (visitorAmount<maxAmount):
            visitorAmount += randint(0,3)
        else:
            visitorAmount -= randint(0,3)
    return visitorAmount

def getPeopleStr():
    return str(generatePeople())

def getPeopleInt():
    return int(generatePeople())

def setMax(Amount):
    maxAmount = Amount
    
