import pygame

try:
    spaceSimImg = pygame.image.load("data/space-sim.PNG")
    merryGoRoundImg = pygame.image.load("data/merry-go-round.PNG")
    waterSlideImg = pygame.image.load("data/water_slide.png")
    hauntedMansionImg = pygame.image.load("data/haunted-mansion.PNG")
    grassTileImg = pygame.image.load("data/grasstile.png")
    mazeImg = pygame.image.load("data/maze.png")
    upImg = pygame.image.load("data/up.png")
    downImg = pygame.image.load("data/down.png")
    observatoryImg = pygame.image.load("data/observatory.png")
    dolphinShowImg = pygame.image.load("data/dolphin-show.png")
except:
    print("error loading images")


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
    elif(name=="grassTileImg"):
        return grassTileImg
    elif(name=="mazeImg"):
        return mazeImg
    elif(name=="upImg"):
        return upImg
    elif(name=="downImg"):
        return downImg
    elif(name=="observatoryImg"):
        return observatoryImg
    elif(name=="dolphinShowImg"):
        return dolphinShowImg
