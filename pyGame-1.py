#!/usr/bin/python
import pygame,os,sys
from pygame.locals import *
from clAttraction import Attraction

xres = 640
yres = 480
screen = pygame.display.set_mode((xres, yres))
screen.fill((255,255,255))

def makeGrid():
    for x in range(0,640,10):
        x = x + 10
        pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
        
        
    for y in range(0,480,10):
        y = y + 10
        pygame.draw.line(screen,(255,0,0),(0,y), (xres,y),1)
        pygame.display.flip()
        done = 0
        
def fillSquare(event):
    attr1 = Attraction(5,5)
    
    h=0
    yp = (event.pos[1]/10)*10+1 #1 is the y position

    while h <= attr1.getHeight():
        xp = (event.pos[0]/10)*10+1 #0 is the x position
        rectange = (xp,yp,10,10)
        w=0
        while w <= attr1.getWidth():
            pygame.draw.rect(screen, (0, 255, 0), (xp, yp, 9, 9))
            xp += 10
            w+=1
        yp+=10
        h+=1
    
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
                     print "left button clicked"
                     fillSquare(e)
                 elif e.button == 2:
                     print "middle button clicked"
                 elif e.button == 3:
                     print "right button clicked"
                 elif e.button == 4:
                     print "scrolling forward"
                 elif e.button == 5:
                     print "scrolling backward"
                 else:
                     print "some cool button"
                 print e.pos
        if done:
            break
            


if __name__ == "__main__":
   main()
