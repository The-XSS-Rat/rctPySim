#Attraction class
class Attraction:
        squaresWidth = 4
        squaresHeight = 4
        cost = 50
        color = (0,255,0)
        
        def __init__(self,width,height,color,currAtrrCost):
                self.squaresHeight = height
                self.squaresWidth = width
                self.color = color
                self.cost = currAtrrCost
                
        def getHeight(self):
                return self.squaresHeight
                
        def getWidth(self):
                return self.squaresWidth
                
        def getColor(self):
                return self.color

        def getCost(self):
                return self.cost
