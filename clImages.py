import pygame

spaceSimImg = pygame.image.load("data/space-sim.PNG")
merryGoRoundImg = pygame.image.load("data/merry-go-round.PNG")
waterSlideImg = pygame.image.load("data/water_slide.png")

def getImage(name):
    global merryGoRoundImg,spaceSimImg
    if(name=="merryGoRoundImg"):
        return merryGoRoundImg
    elif(name=="spaceSimImg"):
        return spaceSimImg
    elif(name=="waterSlideImg"):
        return waterSlideImg
