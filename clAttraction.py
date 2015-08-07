#Attraction class
class Attraction:
	squaresWidth = 4
	squaresHeight = 4
	cost = 50
	
	def __init__(self,width,height):
		self.squaresHeight = height
		self.squaresWidth = width
		
	def getHeight(self):
		return self.squaresHeight
		
	def getWidth(self):
		return self.squaresWidth
