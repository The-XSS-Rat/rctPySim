#!/usr/bin/python
import pygame,os,sys
from pygame import *
from clAttraction import Attraction
from clPeople import *
from clPlayer import *
import time

xres = 840
gameXRes = 640
yres = 480

Attractions = []
Grid = []

currAttr = "Marry-go-round"
currAttrWidth = 2
currAttrHeight = 2
currAttrColor = (0, 255, 0)
addedPeople = 1
maxPeopleAdded = 3
currAtrrCost = 4500

screen = pygame.display.set_mode((xres, yres))
screen.fill((255,255,255))

def makeGrid():
    global Grid

    for x in range(70,gameXRes+10,10):
        pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
        x = x + 10
        
    for y in range(0,490,10):
        pygame.draw.line(screen,(255,0,0),(70,y), (gameXRes,y),1)
        y = y + 10
        done = 0
    Grid = [[0 for x in range(int(gameXRes/10))] for y in range(int(yres/10))]
    # Do not know why this is in here: Grid[30][15] = 1
    fillMenu()
    pygame.display.flip()
        

def fillMenu():
    myfont = pygame.font.SysFont("monospace", 10)

    # Ferris-Wheel
    pygame.draw.rect(screen,(204,0,102),(0,0,20,20))
    labelTextAttrRC = myfont.render("Ferris-", 1, (0,0,0))
    labelTextAttrRC2 = myfont.render("Wheel", 1, (0,0,0))
    labelPriceAttrRC = myfont.render("€ 1.500", 1, (0,0,0))
    screen.blit(labelTextAttrRC, (0, 20))
    screen.blit(labelTextAttrRC2, (0, 30))
    screen.blit(labelPriceAttrRC, (0, 40))
    
    # Haunted Mansion
    pygame.draw.rect(screen,(255,255,0),(0,70,20,20))
    labelTextAttrRC = myfont.render("Haunted-", 1, (0,0,0))
    labelTextAttrRC2 = myfont.render("Mansion", 1, (0,0,0))
    labelPriceAttrRC = myfont.render("€ 8.500", 1, (0,0,0))
    screen.blit(labelTextAttrRC, (0, 90))
    screen.blit(labelTextAttrRC2, (0, 100))
    screen.blit(labelPriceAttrRC, (0, 110))
    
    # Roller Coaster
    pygame.draw.rect(screen,(61,7,12),(0,140,20,20))
    # render text
    labelTextAttrRC = myfont.render("Roller-", 1, (0,0,0))
    labelTextAttrRC2 = myfont.render("Coaster", 1, (0,0,0))
    labelPriceAttrRC = myfont.render("€ 13.000", 1, (0,0,0))
    screen.blit(labelTextAttrRC, (0, 160))
    screen.blit(labelTextAttrRC2, (0, 170))
    screen.blit(labelPriceAttrRC, (0, 180))
    

def fillSquare(event):
    global currAttrWidth
    global currAttr
    global currAttrHeight
    global currAttrColor
    global Grid
    global addedPeople
    global maxPeopleAdded
    global currAtrrCost
    
    
    Attractions.append(Attraction(currAttrWidth,currAttrHeight,currAttrColor,currAtrrCost))
    attr1 = Attractions[len(Attractions)-1]

    h=0
    yp = int(event.pos[1]/10)*10 + 1#1 is the y position
    orgXP = int(event.pos[0]/10)*10
    if orgXP >= 70:
        while h <= attr1.getHeight():
            xp = int(event.pos[0]/10)*10 + 1#0 is the x position
            rectange = (xp,yp,10,10)
            w=0
            while w <= attr1.getWidth():
                try:
                    if Grid[int(yp/10)][int(xp/10)] == 1:
                        print("Er kan hier geen blok van deze grote worden geplaatst. Er staat reeds een blok in de weg./ No blocked can be placed here, already a block underlying")
                        return
                    else:
                        xp += 10
                        w+=1
                except:
                    print("Er kan hier geen blok van deze grote worden geplaatst. Dit valt buiten het venster/No blocked can be placed here, outside of window space")
                    return
            yp+=10
            h+=1
        h=0
        yp = int(event.pos[1]/10)*10 + 1#1 is the y position
        orgXP = int(event.pos[0]/10)*10
        
        # substract the amount from players cash
        if(getCashInt()>=attr1.getCost()):
            while h <= attr1.getHeight():
                xp = int(event.pos[0]/10)*10 + 1#0 is the x position
                rectange = (xp,yp,10,10)
                w=0
                while w <= attr1.getWidth():
                    try:
                        pygame.draw.rect(screen, attr1.getColor(), (xp, yp, 9, 9))
                        Grid[int(yp/10)][int(xp/10)] = 1
                        xp += 10
                        w+=1
                    except:
                        print("Fout bij het plaatsen van blok./Error placing block.")
                        break
                yp+=10
                h+=1
            lowerCash(attr1.getCost())
            setMaxVisitors(maxPeopleAdded)
            AddToVisitors(addedPeople)
        else:
            print("Niet genoeg geld/Not enough cash")
        
    else:
        print("menu tapped")
        #attraction list
        if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
            currAttr = "Ferris-wheel"
            currAttrWidth = 2
            currAttrHeight = 4
            currAttrColor = (204,0,102)
            addedPeople = 5
            maxPeopleAdded = 10
            currAtrrCost = 1500

        if orgXP>=0 and orgXP<=20 and yp>=70 and yp<=90:
            currAttr = "Haunted house"
            currAttrWidth = 3
            currAttrHeight = 4
            currAttrColor = (255,255,0)
            addedPeople = 20
            maxPeopleAdded = 20
            currAtrrCost = 8500
        if orgXP>=0 and orgXP<=20 and yp>=140 and yp<=160:
            currAttr = "Roller Coaster"
            currAttrWidth = 8
            currAttrHeight = 5
            currAttrColor = (61,7,12)
            addedPeople = 100
            maxPeopleAdded = 200
            currAtrrCost = 13000

    pygame.display.flip()
    
#The main loop
def main():
    pygame.font.init()
    x = 10
    y = 10
    #  pygame.draw.rect(screen,(0,0,255),(50,50,50,50),1)
    #vertical lines
    #pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
    
    #horizontal lines
    #pygame.draw.line(screen,(255,0,0),(0,10),(gameXRes,y),1)
    
    done = 0
    
    makeGrid()
    
    while 1:
        time.sleep(0.1)
        generateCash()
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 15)

        # Erase previous labels
        pygame.draw.rect(screen,(255,255,255),(641,0,740,100))

        # render text
        labelTextVisitors = myfont.render("Num. of visitors", 1, (0,0,0))
        labelCounterVisitors = myfont.render(getPeopleStr(), 1, (0,0,0))
        labelTextMoney= myfont.render("Money", 1, (0,0,0))
        labelCounterMoney = myfont.render(getCashStr(), 1, (0,0,0))
        screen.blit(labelTextVisitors, (640, 0))
        screen.blit(labelCounterVisitors, (640, 13))
        screen.blit(labelTextMoney, (640, 26))
        screen.blit(labelCounterMoney, (640, 39))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                 
                 if e.button == 1:
                     print("left button clicked")
                     fillSquare(e)
                 elif e.button == 2:
                     print("middle button clicked")
                 elif e.button == 3:
                     print("right button clicked")
                 elif e.button == 4:
                     print("scrolling forward")
                 elif e.button == 5:
                     print("scrolling backward")
                 else:
                     print("some cool button")
                 print(e.pos)
        if done:
            break

if __name__ == "__main__":
   main()
