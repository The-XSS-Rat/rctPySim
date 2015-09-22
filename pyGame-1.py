#!/usr/bin/python
import pygame,os,sys
from pygame import *
from clAttraction import Attraction

xres = 640
yres = 480

Attractions = []

currAttr = "Marry-go-round"
currAttrWidth = 5
currAttrHeight = 10
currAttrColor = (0, 255, 0)


screen = pygame.display.set_mode((xres, yres))
screen.fill((255,255,255))

def makeGrid():
    for x in range(0,640,10):
        x = x + 10
        print(x)
        pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
        
        
    for y in range(0,480,10):
        y = y + 10
        pygame.draw.line(screen,(255,0,0),(0,y), (xres,y),1)
        done = 0
    pygame.draw.line(screen,(0,0,255),(70,0),(70,yres),3)
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

    Attractions = Attraction(currAttrWidth,currAttrHeight,currAttrColor)
    attr1 = Attractions[len(Attractions)]

    h=0
    yp = int(event.pos[1]/10)*10 + 1#1 is the y position
    orgXP = int(event.pos[0]/10)*10
    if orgXP >= 70:
        while h <= attr1.getHeight():
            xp = int(event.pos[0]/10)*10 + 1#0 is the x position
            print("xp=" + str(xp))

            rectange = (xp,yp,10,10)
            w=0
            while w <= attr1.getWidth():
                pygame.draw.rect(screen, attr1.getColor(), (xp, yp, 9, 9))
                xp += 10
                w+=1
            yp+=10
            h+=1
    else:
        print("menu tapped")
        if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
            currAttr = "Ferris-wheel"
            currAttrWidth = 2
            currAttrHeight = 4
            currAttrColor = (255,0,0)

        if orgXP>=0 and orgXP<=20 and yp>=30 and yp<=50:
            currAttr = "Haunted house"
            currAttrWidth = 1
            currAttrHeight = 8
            currAttrColor = (0,0,255)

    pygame.display.flip()
    
#The main loop
def main():
    x = 10
    y = 10
#  pygame.draw.rect(screen,(0,0,255),(50,50,50,50),1)
#vertical lines
    pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
    
#horizontal lines
    pygame.draw.line(screen,(255,0,0),(0,10),(xres,y),1)
    
    pygame.display.flip()
    done = 0
    
    makeGrid()
        
    while 1:
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
