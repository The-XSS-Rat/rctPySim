#!/usr/bin/python
import pygame,os,sys
from pygame import *
from clAttraction import Attraction
from clPeople import *
import time

xres = 740
gameXRes = 640
yres = 480

Attractions = []
Grid = []

currAttr = "Marry-go-round"
currAttrWidth = 5
currAttrHeight = 10
currAttrColor = (0, 255, 0)


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
    Grid[30][15] = 1
    print(Grid)
    fillMenu()
    pygame.display.flip()
        

def fillMenu():
    pygame.draw.rect(screen,(204,0,102),(0,0,20,20))
    pygame.draw.rect(screen,(255,255,0),(0,30,20,20))

def fillSquare(event):
    global currAttrWidth
    global currAttr
    global currAttrHeight
    global currAttrColor
    global Grid
    
    Attractions.append(Attraction(currAttrWidth,currAttrHeight,currAttrColor))
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
                        print("Er kan hier geen blok van deze grote worden geplaatst. Er staat reeds een blok in de weg.")
                        return
                    else:
                        xp += 10
                        w+=1
                except:
                    print("Er kan hier geen blok van deze grote worden geplaatst. Dit valt buiten het venster")
                    return
            yp+=10
            h+=1
        h=0
        yp = int(event.pos[1]/10)*10 + 1#1 is the y position
        orgXP = int(event.pos[0]/10)*10
    
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
                    print("Fout bij het plaatsen van blok.")
                    break
            yp+=10
            h+=1
    else:
        print("menu tapped")
        if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
            currAttr = "Ferris-wheel"
            currAttrWidth = 2
            currAttrHeight = 4
            currAttrColor = (204,0,102)

        if orgXP>=0 and orgXP<=20 and yp>=30 and yp<=50:
            currAttr = "Haunted house"
            currAttrWidth = 1
            currAttrHeight = 8
            currAttrColor = (255,255,0)

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
        time.sleep(0.16)
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 15)

        # Erase previous labels
        pygame.draw.rect(screen,(255,255,255),(641,12,660,20))

        # render text
        labelTextVisitors = myfont.render("Num. of users", 1, (0,0,0))
        labelCounterVisitors = myfont.render(getPeopleStr(), 1, (0,0,0))
        screen.blit(labelTextVisitors, (640, 0))
        screen.blit(labelCounterVisitors, (640, 12))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
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
