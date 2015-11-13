#!/usr/bin/python
from random import randint
import locale
from clPeople import getPeopleInt

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
        playerCash += randint(0,1) * getPeopleInt() * modifier

def setLoan(Amount):
    global loan
    loan = Amount
    
def setLoanLimit(Amount):
    global loanLimit
    loanLimit = Amount

def addLoan(Amount):
    global loan
    message = "+ €1.000 geleend/loaned"
    if(loan + Amount > loanLimit):
        message = "Je kan niet meer dan " + str(locale.currency(loanLimit,grouping=True)) + " lenen"
    else:
        loan += Amount
    return message
    
def lowerLoan(Amount):
    global loan
    AmountWithdrawn = 0
    if(loan - Amount < 0):
        AmountWithdrawn = loan
        loan = 0
    else:
        loan -= Amount
        AmountWithdrawn = Amount
    return int(AmountWithdrawn)
    
def getIntLoan():
    global loan
    return int(loan)
    
def getStrLoan():
    global loan
    return str(locale.currency(loan,grouping=True))
    
