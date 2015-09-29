#!/usr/bin/python
from random import randint

visitorAmount = 0
maxAmount = 45

chanceOfPlus = 55

def generatePeople():
    global chanceOfPlus
    global chanceOfMinus
    global visitorAmount

    chancePlusMinus = randint(0,100)
    
    if(randint(0,1000) < 200):
        if chancePlusMinus >= (100 - chanceOfPlus) and (visitorAmount<maxAmount):
            visitorAmount += randint(0,3)
        else:
            visitorAmount -= randint(0,3)
        if visitorAmount < 0 : visitorAmount = 0
    return visitorAmount

def getPeopleStr():
    return str(generatePeople())

def getPeopleInt():
    return int(generatePeople())

def setMaxVisitors(Amount):
    global maxAmount
    maxAmount += Amount

def AddToVisitors(Amount):
    global visitorAmount
    visitorAmount += Amount


    
