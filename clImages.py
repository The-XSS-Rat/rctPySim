import pygame

spaceSimImg = pygame.image.load("data/space-sim.PNG")
merryGoRoundImg = pygame.image.load("data/merry-go-round.PNG")
waterSlideImg = pygame.image.load("data/water_slide.png")
hauntedMansionImg = pygame.image.load("data/haunted-mansion.PNG")


def getImage(name):
    global merryGoRoundImg,spaceSimImg
    if(name=="merryGoRoundImg"):
        return merryGoRoundImg
    elif(name=="spaceSimImg"):
        return spaceSimImg
    elif(name=="waterSlideImg"):
        return waterSlideImg
    elif(name=="hauntedMansionImg"):
        return hauntedMansionImg
