#!/usr/bin/python
from random import randint

visitorAmount = 0

def generatePeople():
    global visitorAmount
    if(randint(0,900) < 5):
        visitorAmount += randint(0,3)
    return visitorAmount

def getPeopleStr():
    return str(generatePeople())

def getPeopleInt():
    return int(generatePeople())
