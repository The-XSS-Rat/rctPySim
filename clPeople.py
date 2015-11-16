#!/usr/bin/python
from random import randint

visitorAmount = 0
maxAmount = 45
Happyness = 20
chanceOfPlus = 55

def generatePeople():
    global chanceOfPlus
    global chanceOfMinus
    global visitorAmount

    chancePlusMinus = randint(0,100)
    
    if(randint(0,1000) < 100):
        if chancePlusMinus >= (100 - chanceOfPlus) and (visitorAmount<maxAmount):
            visitorAmount += randint(0,10)
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

def removeVisitors(Amount):
    global visitorAmount
    if(visitorAmount-Amount<0):
        visitorAmount = 0
    else:
        visitorAmount -= Amount

def getVisitorAmount():
    return visitorAmount
    
def getHappyness():
    return Happyness
    
def setChanceOfPlus(Amount):
    global chanceOfPlus
    chanceOfPlus = Amount
    
def setHappyness(Amount):
    global Happyness
    Happyness = Amount
    
def addHappyness(Amount):
    global Happyness
    if(Happyness+Amount >=100):
        Happyness = 100
    else:
        Happyness += Amount
    
def removeHappyness(Amount):
    global Happyness
    if(Happyness-Amount <=0):
        Happyness = 0
    else:
        Happyness -= Amount
    

    
