#!/usr/bin/python
from random import randint
import locale
from clPeople import getPeopleInt,getHappyness

locale.setlocale( locale.LC_ALL, '' )

playerCash = 4500
loan = 4000
modifier = 1
loanLimit = 15000

def getCashStr():
    return str(locale.currency(playerCash,grouping=True))

def getCashInt():
    return int(playerCash)

def addCash(Amount):
    global playerCash
    playerCash += Amount
    
def setModifier(Amount):
    global modifier
    modifier += Amount

def lowerCash(Amount):
    global playerCash
    playerCash -= Amount

def generateCash():
    global playerCash
    global modifier
    if(randint(0,100)<10):
        playerCash += randint(0,1) * getPeopleInt() * modifier * (getHappyness()/10)

def setLoan(Amount):
    global loan
    loan = Amount
    
def setLoanLimit(Amount):
    global loanLimit
    loanLimit = Amount

def addLoan(Amount):
    global loan
    message = "Loaned + €1.000"
    if(loan + Amount > loanLimit):
        message = "You can not loan more then " + str(locale.currency(loanLimit,grouping=True))
    else:
        loan += Amount
    return message
    
def lowerLoan(Amount):
    global loan
    message = "You can't pay back any more of your loan"
    AmountWithdrawn = 0
    if(loan - Amount < 0):
        AmountWithdrawn = loan
        message = "You can't pay back any more of your loan"
        loan = 0
    else:
        loan -= Amount
        message = "You've payed back - " + str(locale.currency(Amount,grouping=True))
        AmountWithdrawn = Amount
    return {"withdrawn":int(AmountWithdrawn),"message":message}
    
def getIntLoan():
    global loan
    return int(loan)
    
def getStrLoan():
    global loan
    return str(locale.currency(loan,grouping=True))
    
