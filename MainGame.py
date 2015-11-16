#!/usr/bin/python3.2.4
#DONE: Make a grassy tilefor the backdrop
#DONE: Make the menu switchable with buttons (attractions/scenary/shows/...)
#DONE: Build in objectives
#DONE: Right click needs to blit grass tiles instead of white BG
#DONE: Make a main menu
#DONE: Adept difficulty
#DONE: Make a decorations module
#DONE: Make the random objective button function(possibly random, possible not random)
#DONE: build in menu options
#DONE: Added loans
#DONE: Add visitor happyness stats
#DONE: Refine visitor happyness stats - Add more happyness when adding attraction
#DONE: Refine visitor happyness stats - Add more happyness when adding scenery



#TODO: REFINE: Add money to user for destroying building(already implemented but i want to give less money when the building is older.
#TODO: Refine the money making process
#TODO: Refine the random objective(i.e. number of attractions before time-unit/Pay off loan by(+ have x amount of money))
#TODO: Make game scaleable(ui)
#TODO: Refine: Adept difficulty
#TODO: Expand a main menu
#TODO: Make main menu better looking
#TODO: Make moving sprites by using a general function
#TODO: Fill in the decorations menu
#TODO: Add more attractions
#TODO: Add random R&D(research a new attraction, with a fail chance depending on the amount of money you put towards it)
#TODO: Add visitor happyness stats
#TODO: Add more scenery
#TODO: Add roads
#TODO: Refine visitor happyness stats - Remove happyness when removing an attraction
#TODO: Refine visitor happyness stats - Add more happyness when roads are put to attractions
#TODO: Refine visitor happyness stats - Add more happyness when scenery is grouped closer togheter
#TODO: Resize board on difficulty changes
#TODO: Remove the default attraction when none is selected
#TODO: Make it so that attractions need to be selected multiple times if wanting to put down more
#TODO: Make it so that when you select an attraction, You see a preview and information in the message window


import pygame,os,sys
try:
    import pygame._view
except:
    pass
from pygame import *
from clAttraction import Attraction
from clPeople import *
from clImages import *
from clPlayer import *
import pygame._view
import time

xres = 840
gameXRes = 640
yres = 550
gameYRes = 480
sysMenuStart = 630
attrMenuEnd = 70
Screenmode = "MM" # Main menu

clockticks=0
targetClockTick = 10000
moneyTarget = 100000
goalType = "moneyTicks"
visitorTarget = 0

Attractions = []
Grid = []
Blocks = []
currMenu = "Attractions1"

currAttr = "Marry-go-round"
currAttrWidth = 2
currAttrHeight = 2
currAttrColor = (0, 255, 0)
addedPeople = 1
addedHappyness = 1
maxPeopleAdded = 3
currAtrrCost = 4500

image = getImage("merryGoRoundImg")


screen = pygame.display.set_mode((xres, yres))
screen.fill((255,255,255))

def makeGrid():
    global Grid
    
    for x in range (70,gameXRes,10):
        for y in range (0,gameYRes,10):
            screen.blit(pygame.transform.scale(getImage("grassTileImg"),(10,10)),(x,y))
    Grid = [[0 for x in range(int(gameXRes/10))] for y in range(int(gameYRes/10))]
    fillMenu()
    pygame.display.flip()
    
def displayMessage(line1,line2="",line3="",typeOfMsg="Info"):
    pygame.draw.rect(screen,(255,255,255),(4,484,546,60))
    
    messageFont = pygame.font.SysFont("ariel", 15)
    messageFont.set_bold(True)
    
    if(typeOfMsg=="Warning" or typeOfMsg=="Error"):
        msglabel1 = messageFont.render(line1,1,(255,0,0))
        msglabel2 = messageFont.render(line2,1,(255,0,0))
        msglabel3 = messageFont.render(line3,1,(255,0,0))
    elif(typeOfMsg=="Info"):
        msglabel1 = messageFont.render(line1,1,(0,0,0))
        msglabel2 = messageFont.render(line2,1,(0,0,0))
        msglabel3 = messageFont.render(line3,1,(0,0,0))
    screen.blit(msglabel1,(20,490))
    screen.blit(msglabel2,(20,505))
    screen.blit(msglabel3,(20,520))

def makeMainMenu():
    menuFont = pygame.font.SysFont("ariel", 15)

    infolabel1 = menuFont.render("Choose a dificulty to start:",1,(0,0,0))
    screen.blit(infolabel1,(10,10))

    pygame.draw.rect(screen,(0,0,0),(10,25,40,15))
    pygame.draw.rect(screen,(0,0,0),(10,41,40,15))
    pygame.draw.rect(screen,(0,0,0),(10,57,40,15))
    startGameLabelE = menuFont.render("EASY",1,(255,255,255))
    startGameLabelM = menuFont.render("MEDI",1,(255,255,255))
    startGameLabelH = menuFont.render("HARD",1,(255,255,255))
    screen.blit(startGameLabelE,(12,28))
    screen.blit(startGameLabelM,(12,44))
    screen.blit(startGameLabelH,(12,60))
    
    pygame.display.flip()

def makeMenuItemAttractions(screen,w,h,xs,ys,t1x,t1y,t2x,t2y,t3x,t3y,txt1,txt2,txt3,imgName):
    myfont = pygame.font.SysFont("ariel", 15)
    screen.blit(pygame.transform.scale(getImage(imgName),(w,h)),(xs,ys))
    labelTextAttrRC = myfont.render(txt1, 1, (0,0,0))
    labelTextAttrRC2 = myfont.render(txt2, 1, (0,0,0))
    labelPriceAttrRC = myfont.render(txt3, 1, (0,0,0))
    screen.blit(labelTextAttrRC, (t1x,t1y))
    screen.blit(labelTextAttrRC2, (t2x, t2y))
    screen.blit(labelPriceAttrRC, (t3x, t3y))
    
def makeMenuItemDecorations(screen,w,h,xs,ys,t1x,t1y,t2x,t2y,txt1,txt2,imgName):
    myfont = pygame.font.SysFont("ariel", 15)
    screen.blit(pygame.transform.scale(getImage(imgName),(w,h)),(xs,ys))
    labelTextAttrRC = myfont.render(txt1, 1, (0,0,0))
    labelPriceAttrRC = myfont.render(txt2, 1, (0,0,0))
    screen.blit(labelTextAttrRC, (t1x,t1y))
    screen.blit(labelPriceAttrRC, (t2x, t2y))
    
def drawProgressBar(value):
    myfont = pygame.font.SysFont("ariel", 15)
    visitorHappynessLabel = myfont.render("Visitor Happyness",1,(0,0,0))
    screen.blit(visitorHappynessLabel,(642,200))

    pygame.draw.rect(screen,(255,0,0),(642,220,180,20))
    width = int(value)*180/100
    pygame.draw.rect(screen,(0,255,0),(642,220,width,20))
    
def cleanAttraction():
    global currAttr,currAttrWidth,currAttrHeight,currAttrColor,addedPeople,addedHappyness,image,maxPeopleAdded,currAtrrCost
    currAttr = ""
    currAttrWidth = 0
    currAttrHeight = 0
    currAttrColor = ""
    addedPeople = 0
    addedHappyness = 0
    image = ""
    maxPeopleAdded = 0
    currAtrrCost = 0
    pygame.draw.rect(screen,(255,255,255),(4,484,546,60))


def fillMenu():  
    global currMenu
    
    pygame.draw.rect(screen,(255,255,255),(0,0,70,480))
    
    myfont = pygame.font.SysFont("ariel", 15)
    myfontLoans = pygame.font.SysFont("ariel", 30)
    
    #righthandSide menu
    labelLoan = myfont.render("Loan: " + getStrLoan(), 1, (0,0,0))
    labelLoanAdd = myfontLoans.render("+", 1, (0,0,0))
    labelLoanRemove = myfontLoans.render("-", 1, (0,0,0))
    screen.blit(labelLoan, (sysMenuStart+41, 420))
    screen.blit(labelLoanAdd, (sysMenuStart+12, 410))
    screen.blit(labelLoanRemove, (sysMenuStart+28, 410))
    pygame.draw.rect(screen,(0,0,0),(sysMenuStart+10,413,15,15),2)
    pygame.draw.rect(screen,(0,0,0),(sysMenuStart+25,413,15,15),2)

    #random challenge
    screen.blit(pygame.transform.scale(getImage("randomHatImg"),(20,20)),(sysMenuStart+10,430))
    labelText = myfont.render("Generate a", 1, (0,0,0))
    labelText2 = myfont.render("Random challenge", 1, (0,0,0))
    screen.blit(labelText, (sysMenuStart+10, 450))
    screen.blit(labelText2, (sysMenuStart+10, 460))

    if(currMenu=="Attractions1"):
        #makeMenuItem(screen,w,h,xs,ys,t1x,t1y,t2x,t2y,t3x,t3y,txt1,txt2,txt3,imgName)
        makeMenuItemAttractions(screen,20,20,0,0,0,20,0,30,0,40,"Merry-go-","Round","€ 1.500","merryGoRoundImg")
        makeMenuItemAttractions(screen,20,20,0,70,0,90,0,100,0,110,"Space-","Sim","€ 3.200","spaceSimImg")
        makeMenuItemAttractions(screen,20,20,0,140,0,160,0,170,0,180,"Haunted-","Mansion","€ 4.500","hauntedMansionImg")
        makeMenuItemAttractions(screen,20,20,0,210,0,230,0,240,0,250,"Water-","Slide","€ 13.500","waterSlideImg")
        makeMenuItemAttractions(screen,20,20,0,280,0,300,0,310,0,320,"Hedge-","Maze","€ 2.500","mazeImg")
        makeMenuItemAttractions(screen,20,20,0,350,0,370,0,380,0,390,"Obser-","vatory","€ 500","observatoryImg")
        #Down arrow
        screen.blit(pygame.transform.scale(getImage("downImg"),(20,20)),(0,460))
        #Decorations button
        screen.blit(pygame.transform.scale(getImage("btnDecoration"),(20,20)),(40,460))
    elif(currMenu=="Attractions2"):
        makeMenuItemAttractions(screen,20,20,0,0,0,20,0,30,0,40,"Dolphin-","Show","€ 14.500","dolphinShowImg")
        makeMenuItemAttractions(screen,20,20,0,70,0,90,0,100,0,110,"Concert","Show","€ 800","concert")
        makeMenuItemAttractions(screen,20,20,0,140,0,160,0,170,0,180,"Arcade","Center","€ 1.000","arcadeImg")
        #UP & DOWN arrows
        #screen.blit(pygame.transform.scale(getImage("downImg"),(20,20)),(0,460))
        screen.blit(pygame.transform.scale(getImage("upImg"),(20,20)),(20,460))
        screen.blit(pygame.transform.scale(getImage("btnDecoration"),(20,20)),(40,460))

    elif(currMenu=="Decoration"):
        #def makeMenuItemDecorations(screen,w,h,xs,ys,t1x,t1y,t2x,t2y,txt1,txt2,imgName):
        #Tree1
        makeMenuItemDecorations(screen,20,20,0,0,0,20,0,30,"Tree-1","€ 100","tree1")
        #Boom 2
        makeMenuItemDecorations(screen,20,20,0,60,0,80,0,90,"Tree-2","€ 200","tree2")
        #Tree 3
        makeMenuItemDecorations(screen,20,20,0,120,0,140,0,150,"Tree-3","€ 350","tree3")
        #Paths
        makeMenuItemDecorations(screen,20,20,0,180,0,200,0,210,"Path","€ 50","pathImg")
        screen.blit(pygame.transform.scale(getImage("btnAttractions"),(20,20)),(40,460))
        
    elif(currMenu=="Shows"):#FILlER CODE
        # Dolphin show
        #pygame.draw.rect(screen,(204,0,102),(0,0,20,20))
        screen.blit(pygame.transform.scale(getImage("merryGoRoundImg"),(20,20)),(0,0))
        labelTextAttrRC = myfont.render("Merry-go-", 1, (0,0,0))
        labelTextAttrRC2 = myfont.render("Round", 1, (0,0,0))
        labelPriceAttrRC = myfont.render("€ 1.500", 1, (0,0,0))
        screen.blit(labelTextAttrRC, (0, 20))
        screen.blit(labelTextAttrRC2, (0, 30))
        screen.blit(labelPriceAttrRC, (0, 40))
        screen.blit(pygame.transform.scale(getImage("upImg"),(20,20)),(20,460))
    
def mainMenuClick(event):
    global Screenmode
    
    yp = event.pos[1]
    xp = event.pos[0]
    
    if(yp>=25 and yp<= 40 and xp >=10 and xp <= 50):
        Screenmode = "MG;E"
        addCash(10000)
        AddToVisitors(60)
        setModifier(2)
        addLoan(1000)
        setLoanLimit(100000)
        setChanceOfPlus(51)
        makeGrid()
    elif(yp>=41 and yp<= 56 and xp >=10 and xp <= 50):
        Screenmode = "MG;M"
        addCash(4000)
        addLoan(4000)
        setLoanLimit(50000)
        setModifier(1.5)
        AddToVisitors(60)
        setChanceOfPlus(45)
        makeGrid()
    elif(yp>=57 and yp<= 82 and xp >=10 and xp <= 50):
        Screenmode = "MG;H"
        addLoan(10000)
        makeGrid()
    print(Screenmode)

def setAttraction(currAttrF,currAttrWidthF,currAttrHeightF,currAttrColorF,addedPeopleF,addedHappynessF,imageF,maxPeopleAddedF,currAtrrCostF):
    global currAttr,currAttrWidth,currAttrHeight,currAttrColor,addedPeople,addedHappyness,image,maxPeopleAdded,currAtrrCost
    
    currAttr = currAttrF
    currAttrWidth = currAttrWidthF
    currAttrHeight = currAttrHeightF
    currAttrColor = currAttrColorF
    addedPeople = addedPeopleF
    addedHappyness = addedHappynessF
    image = imageF
    maxPeopleAdded = maxPeopleAddedF
    currAtrrCost = currAtrrCostF
    displayAttractionMsg(imageF,currAttrF,currAtrrCost)

def displayAttractionMsg(img,currAttrF,currAtrrCostF):
    myfont = pygame.font.SysFont("ariel", 15)
    pygame.draw.rect(screen,(255,255,255),(4,484,546,60))
    screen.blit(pygame.transform.scale(img,(40,40)),(20,500))
    labelTextAttrRC = myfont.render(currAttr, 1, (0,0,0))
    labelPriceAttrRC = myfont.render(str(locale.currency(currAtrrCost,grouping=True)), 1, (0,0,0))
    labelTextAttrSpace = myfont.render("Takes up " + str(currAttrWidth) + "x" + str(currAttrHeight) + " Spaces", 1, (0,0,0))
    screen.blit(labelTextAttrRC, (80, 500))
    screen.blit(labelPriceAttrRC, (80, 515))
    screen.blit(labelTextAttrSpace, (80, 530))
    
def gameLeftClick(event):
    global currAttrWidth
    global currAttr
    global currAttrHeight
    global currAttrColor
    global Grid
    global addedPeople
    global addedHappyness
    global maxPeopleAdded
    global currAtrrCost
    global image
    global Blocks
    global currMenu,sysMenuStart
    
    Attractions.append(Attraction(currAttrWidth,currAttrHeight,currAttrColor,currAtrrCost,image))
    attr1 = Attractions[len(Attractions)-1]
    h=0
    yp = int(event.pos[1]/10)*10 + 1#1 is the y position
    orgXP = int(event.pos[0]/10)*10
    if orgXP >= attrMenuEnd and orgXP <= sysMenuStart:
        if(attr1.getWidth() != 0):

            while h <= attr1.getHeight():
                xp = int(event.pos[0]/10)*10 + 1#0 is the x position
                rectange = (xp,yp,10,10)
                w=0
                while w <= attr1.getWidth():
                    try:
                        if Grid[int(yp/10)][int(xp/10)] == 1:
                            displayMessage("A block of this size can't be placed here","There is already a block in the way","<Warn 01>","Warning")
                            return
                        else:
                            xp += 10
                            w+=1
                    except:
                        displayMessage("A block of this size can't be placed here","It would fall outside of the playing field","<Warn 02>","Warning")
                        return
                yp+=10
                h+=1
            h=0
            yp = int(event.pos[1]/10)*10 + 1#1 is the y position
            orgXP = int(event.pos[0]/10)*10
            
            # substract the amount from players cash if available, else do nothing
            if(getCashInt()>=attr1.getCost()):
                blockText = str(orgXP) + ";" + str(yp) + ";" + str((attr1.getWidth()+1)*10) + ";" + str((attr1.getHeight()+1)*10) + ";" + str(attr1.getCost()) + ";" + str(len(Attractions)-1) + ";n;" + str(addedPeople)
                Blocks.append(blockText)
                screen.blit(pygame.transform.scale(attr1.getImage(),((attr1.getWidth()+1)*10,(attr1.getHeight()+1)*10)),(orgXP,yp))
                while h <= attr1.getHeight():
                    xp = int(event.pos[0]/10)*10 + 1#0 is the x position
                    rectange = (xp,yp,10,10)
                    w=0
                    while w <= attr1.getWidth():
                        try:
                            #pygame.draw.rect(screen, attr1.getColor(), (xp, yp, 9, 9))
                            Grid[int(yp/10)][int(xp/10)] = 1
                            xp += 10
                            w+=1
                        except:
                            displayMessage("Error placing a block","","","Error")
                            break
                    yp+=10
                    h+=1
                lowerCash(attr1.getCost())
                setMaxVisitors(maxPeopleAdded)
                addHappyness(addedHappyness)
                AddToVisitors(addedPeople)
                if(currAttr != "Path"):
                    cleanAttraction()
            else:
                displayMessage("You don't have enough cash","<Info cash>")

    elif orgXP>=sysMenuStart:
        displayMessage("sysMenu clicked","<Info 2>")
        if orgXP >= sysMenuStart+10 and orgXP <= sysMenuStart+10+20 and yp >= 430 and yp <=430+20:
            generateRandomChallenge()
        if orgXP >= sysMenuStart+10 and orgXP <= sysMenuStart+10+15 and yp >=413-5 and yp <= 413+15:
            addLoan(1000)
            addCash(1000)
            displayMessage(addLoan(1000),"","","Info")
        if orgXP >= sysMenuStart+25 and orgXP <= sysMenuStart+25+15 and yp >=413-5 and yp <= 413+15:
            result = lowerLoan(1000)
            lowerCash(int(result['withdrawn']))
            displayMessage(result['message'])
                    
    else:
        print("menu tapped")
        #attraction list
        if(currMenu=="Attractions1"):
            #def setAttraction(currAttrF,currAttrWidthF,currAttrHeightF,currAttrColorF,addedPeopleF,addedHappynessF,imageF,maxPeopleAddedF,currAtrrCostF):
            if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
                setAttraction("Merry-go-round",4,4,(204,0,102),3,1,getImage("merryGoRoundImg"),10,1500)
            if orgXP>=0 and orgXP<=20 and yp>=70 and yp<=90:
                setAttraction("Space Sim",3,3,(255,255,0),10,2,getImage("spaceSimImg"),20,3200)
            if orgXP>=0 and orgXP<=20 and yp>=140 and yp<=160:
                setAttraction("Haunted mansion",6,6,(106,207,72),15,3,getImage("hauntedMansionImg"),50,4500)
            if orgXP>=0 and orgXP<=20 and yp>=210 and yp<=230:
                setAttraction("Water Slide",8,8,(61,7,12),50,9,getImage("waterSlideImg"),200,13000)
            if orgXP>=0 and orgXP<=20 and yp>=280 and yp<=300:
                setAttraction("Maze",5,5,(61,7,12),40,2,getImage("mazeImg"),100,2500)
            if orgXP>=0 and orgXP<=20 and yp>=350 and yp<=370:
                setAttraction("Observatory",4,6,(61,7,12),5,1,getImage("observatoryImg"),30,500)
            #clicking Down menu button    
            if orgXP>=0 and orgXP<=20 and yp>=460 and yp<=480:
                currMenu = "Attractions2"
                fillMenu()
            #Decorations menu
            if orgXP>=40 and orgXP<=60 and yp>=460 and yp<=480:
                currMenu = "Decoration"
                fillMenu()
        elif(currMenu=="Attractions2"):
            if orgXP>=20 and orgXP<=40 and yp>=460 and yp<=480:
                currMenu = "Attractions1"
                fillMenu()
            if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
                setAttraction("Dolphin Show",15,6,(61,7,12),75,11,getImage("dolphinShowImg"),400,14500)
            if orgXP>=0 and orgXP<=20 and yp>=70 and yp<=90:
                setAttraction("Concert show",9,6,(255,255,0),45,9,getImage("concert"),20,10500)
            if orgXP>=0 and orgXP<=20 and yp>=140 and yp<=160:
                setAttraction("Arcade",4,4,(106,207,72),2,2,getImage("arcadeImg"),50,1000)                
            if orgXP>=40 and orgXP<=60 and yp>=460 and yp<=480:
                currMenu = "Decoration"
                fillMenu()
        elif(currMenu=="Decoration"):
            if orgXP>=0 and orgXP<=20 and yp>=0 and yp<=20:
                setAttraction("Tree1",2,3,"",1,1,getImage("tree1"),10,100)
            if orgXP>=0 and orgXP<=20 and yp>=60 and yp<=80:
                setAttraction("Tree2",2,3,"",2,1,getImage("tree2"),12,200)
            if orgXP>=0 and orgXP<=20 and yp>=120 and yp<=140:
                setAttraction("Tree3",2,3,"",3,1,getImage("tree3"),15,350)
            if orgXP>=0 and orgXP<=20 and yp>=180 and yp<=200:
                setAttraction("Path",1,1,"",0,0,getImage("pathImg"),0,50)
            if orgXP>=40 and orgXP<=60 and yp>=460 and yp<=480:
                currMenu = "Attractions1"
                fillMenu()

    pygame.display.flip()

def removeAttraction(event):
    global Blocks
    #print("Blocks", Blocks)
    blockSplitString = []
    #blockText = str(orgXP) + ";" + str(yp) + ";" + str((attr1.getWidth()+1)*10) + ";" + str((attr1.getHeight()+1)*10) + ";" + str(attr1.getCost()) + ";" + str(len(Attractions)-1) + ";n"

    yp = event.pos[1]#1 is the y position
    xp = event.pos[0]
    for idxBlocks, blockstring in enumerate(Blocks):
        blockSplitString.append(blockstring.split(";"))
        for idxBS, blocksplit in enumerate(blockSplitString):
            if(blocksplit[6]=="n"):
                if((xp<(int(blocksplit[0])+int(blocksplit[2])) and xp>int(blocksplit[0])) and (yp<int(blocksplit[1])+int(blocksplit[3])) and yp > int(blocksplit[1])):
                    pygame.draw.rect(screen,(255,255,255),((int(blocksplit[0])),int(blocksplit[1]),int(blocksplit[2]),int(blocksplit[3])))
                    
                            
                    #print(((int(blocksplit[0])),int(blocksplit[1]),(int(blocksplit[0])+int(blocksplit[2])),int(blocksplit[1])+int(blocksplit[3])))
                    #redrawGrid()
                    
                    h=0
                    yp = int(int(blocksplit[1])/10)*10+1#1 is the y position
                    xp = int(int(blocksplit[0])/10)*10
                    
                    for x in range(xp,xp+int(blocksplit[2]),10):
                        for y in range(yp,yp+int(blocksplit[3]),10):
                            screen.blit(pygame.transform.scale(getImage("grassTileImg"),(10,10)),(x,y))
                            #print("xy",x,y)
                            y+=10
                        x+=10
                            
                    h=0
                    yp = int(int(blocksplit[1])/10)*10#1 is the y position
                    xp = int(int(blocksplit[0])/10)*10
                    
                    while h <= int(int(blocksplit[3])/10):
                        xp = int(int(blocksplit[0])/10)*10
                        w=0
                        while w <= int(int(blocksplit[2])/10):
                            #print("ypxp",yp/10,xp/10)
                            if(int(xp/10)<=63):
                                Grid[int(yp/10)][int(xp/10)] = 0
                            #print(int(yp/10),int(xp/10),Grid[int(yp/10)][int(xp/10)])
                            w+=1
                            xp += 10
                        h+=1
                        yp = yp+ 10
                    #print(0.7*int(blocksplit[4]))
                    addCash(0.7*int(blocksplit[4]))
                    removeVisitors(int(int(blocksplit[7])*1.5))
                    Blocks[idxBlocks] = blocksplit[0] + ";" + blocksplit[1] + ";" + blocksplit[2] + ";" + blocksplit[3] + ";" + blocksplit[4] + ";" + blocksplit[5] + ";" + "y" + ";" + blocksplit[7]

def generateRandomChallenge():
    global targetClockTick,moneyTarget,goalType,visitorTarget
    #get money by clocktick
    chanceObjective = randint(0,1)
    if(chanceObjective==0):
        goalType="moneyTicks"
        targetClockTicks = [1000,10000,100000]
        moneyTargets = [50000,100000,10000000]
        
        index = randint(0,len(targetClockTicks)-1)
        
        targetClockTick = clockticks + targetClockTicks[index]
        moneyTarget = getCashInt() + moneyTargets[index]
    else:
        goalType="visitorTicks"
        targetClockTicks = [1000,10000,100000]
        VisitorTargets = [100,1000,95000]
        index = randint(0,len(targetClockTicks)-1)
        
        targetClockTick = clockticks + targetClockTicks[index]
        visitorTarget = getVisitorAmount() + VisitorTargets[index]
        print(visitorTarget)

        

    
    
    
def checkGoal():
    global clockticks,moneyTarget,visitorTarget
    
    myfont = pygame.font.SysFont("ariel", 17)
    if(clockticks>targetClockTick):
        labelTextWon = myfont.render("Failed!!!", 1, (255,0,0))            
        screen.blit(labelTextWon, (640, 400))
    else:
        if(goalType=="moneyTicks"):
            if(getCashInt() >= moneyTarget and clockticks <= targetClockTick):
                labelTextWon = myfont.render("Congratulations!", 1, (0,255,0))            
                screen.blit(labelTextWon, (640, 400))
        if(goalType=="visitorTicks"):
            if(getVisitorAmount() >= visitorTarget and clockticks <= targetClockTick):
                labelTextWon = myfont.render("Congratulations!", 1, (0,255,0))            
                screen.blit(labelTextWon, (640, 400))
            
    
#The main loop
def main():
    global clockticks,visitorTarget,Screenmode
    
    pygame.font.init()
    x = 10
    y = 10
    #  pygame.draw.rect(screen,(0,0,255),(50,50,50,50),1)
    #vertical lines
    #pygame.draw.line(screen,(255,0,0),(x,0),(x,yres),1)
    
    #horizontal lines
    #pygame.draw.line(screen,(255,0,0),(0,10),(gameXRes,y),1)
    
    done = 0
    if(Screenmode=="MM"):
        makeMainMenu()
    else:
        makeGrid()
    
    while 1:
        time.sleep(0.1)
        if("MG" in Screenmode):
            clockticks += 1 
            checkGoal()
            generateCash()
            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
            myfont = pygame.font.SysFont("ariel", 17)

            # Erase previous labels
            pygame.draw.rect(screen,(255,255,255),(641,0,740,300))
            # Draw the messagebox
            pygame.draw.rect(screen,(130,130,130),(0,480,839,70),4)
            # Erase the previous loan box
            pygame.draw.rect(screen,(255,255,255),(sysMenuStart+41,420,100,20))
            #    screen.blit(labelLoan, (sysMenuStart+41, 420))

            # Render Loan
            labelLoan = myfont.render("Loan: " + getStrLoan(), 1, (0,0,0))
            screen.blit(labelLoan, (sysMenuStart+41, 420))
            # render text
            labelTextVisitors = myfont.render("Num. of visitors", 1, (0,0,0))
            labelCounterVisitors = myfont.render(getPeopleStr(), 1, (0,0,0))
            labelTextMoney= myfont.render("Money", 1, (0,0,0))
            labelTextClock= myfont.render("Clockticks", 1, (0,0,0))
            labelTextClockTicks= myfont.render(str(clockticks), 1, (0,0,0))
            labelCounterMoney = myfont.render(getCashStr(), 1, (0,0,0))
            
            screen.blit(labelTextVisitors, (640, 0))
            screen.blit(labelCounterVisitors, (640, 13))
            screen.blit(labelTextMoney, (640, 26))
            screen.blit(labelCounterMoney, (640, 39))
            screen.blit(labelTextClock, (640, 57))
            screen.blit(labelTextClockTicks, (640, 70))
            if(goalType=="visitorTicks"):
                labelGoal = myfont.render("Generate at least", 1, (255,0,0))
                labelGoal2 = myfont.render(str(visitorTarget) + " Visitors", 1, (255,0,0))
                labelGoal3 = myfont.render("By clockTick: ", 1, (255,0,0))
                labelGoal4 = myfont.render(str(targetClockTick), 1, (255,0,0))

            else:
                labelGoal = myfont.render("Generate at least", 1, (255,0,0))
                labelGoal2 = myfont.render(locale.currency(moneyTarget,grouping=True), 1, (255,0,0))
                labelGoal3 = myfont.render("By clockTick: ", 1, (255,0,0))
                labelGoal4 = myfont.render(str(targetClockTick), 1, (255,0,0))
            screen.blit(labelGoal, (640, 120))
            screen.blit(labelGoal2, (640, 133))
            screen.blit(labelGoal3, (640, 146))
            screen.blit(labelGoal4, (640, 159))
            drawProgressBar(getHappyness())
            
            if(clockticks%500==0):
                removeHappyness(5)


        
        
        

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                 
                 if e.button == 1:
                     print("left button clicked")
                     if(Screenmode=="MM"):
                        mainMenuClick(e) 
                     else:
                        gameLeftClick(e)
                 elif e.button == 2:
                     print("middle button clicked")
                 elif e.button == 3:
                     print("right button clicked")
                     removeAttraction(e)
                 elif e.button == 4:
                     print("scrolling forward")
                     addCash(1000)
                 elif e.button == 5:
                     print("scrolling backward")
                     lowerCash(1000)
                 else:
                     print("some cool button")
                 print(e.pos)
        if done:
            break

if __name__ == "__main__":
   main()
