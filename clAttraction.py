#Attraction class
from clImages import *

class Attraction:
        global merryGoRoundImg
        squaresWidth = 4
        squaresHeight = 4
        cost = 50
        color = (0,255,0)
        image = merryGoRoundImg
        
        def __init__(self,width,height,color,currAtrrCost,currImage):
                self.squaresHeight = height
                self.squaresWidth = width
                self.color = color
                self.cost = currAtrrCost
                self.image = currImage
                
        def getHeight(self):
                return self.squaresHeight
                
        def getWidth(self):
                return self.squaresWidth
                
        def getColor(self):
                return self.color

        def getCost(self):
                return self.cost
        
        def setImage(imgFile):
                image = imgFile

        def getImage(self):
                return self.image
