import pygame,sys,os


def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)
    
spaceSimImg = pygame.image.load(find_data_file("data\\space-sim.PNG"))
merryGoRoundImg = pygame.image.load(find_data_file("data\\merry-go-round.PNG"))
waterSlideImg = pygame.image.load(find_data_file("data\\water_slide.png"))
hauntedMansionImg = pygame.image.load(find_data_file("data\\haunted-mansion.PNG"))
grassTileImg = pygame.image.load(find_data_file("data\\grasstile.png"))
mazeImg = pygame.image.load(find_data_file("data\\maze.png"))
upImg = pygame.image.load(find_data_file("data\\up.png"))
downImg = pygame.image.load(find_data_file("data\\down.png"))
observatoryImg = pygame.image.load(find_data_file("data\\observatory.png"))
dolphinShowImg = pygame.image.load(find_data_file("data\\dolphin-show.png"))
randomHatImg = pygame.image.load(find_data_file("data\\random.png"))



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
    elif(name=="randomHatImg"):
        return randomHatImg
        

