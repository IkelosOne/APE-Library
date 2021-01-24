import StandardFunctions
import Maths
import re

class EquationArray():
	def __init__(self,formulaString,startX,endX):
		self.formulaString = formulaString
		self.startX = float(startX)
		self.endX = float(endX)
		self.resolution = 20
		self.array = []
		self.updateArray()


	def updateArray(self):
		# Eventually you will be able to enter an equation in the form y=.x..
		# The resolution is how many points are plotted on the graph. A resolution of 1 means one straight line, 2 means two lines etc.
		# (A resolution of at least 20 is recommended)
		min = self.startX
		max = self.endX
		graphRange = max - min
		gapWidth = graphRange/self.resolution
		self.array = []
		for i in range(round(self.resolution)):
			x = min + gapWidth*i
			equationString = re.sub("x",str(round(x)),self.formulaString)
			answer = Maths.calculateFromString2(equationString)
			self.array.append(answer)


	# Getters
	def get_array(self):
		return self.array

	def get_startX(self):
		return float(self.startX)

	def get_endX(self):
		return float(self.endX)

	# Setters
	def set_startX(self,startX):
		self.min = float(minimum)
		self.updateArray()

	def set_endX(self,endX):
		self.max = float(maximum)
		self.updateArray()

	def set_resolution(self,resolution):
		self.resolution = float(resolution)
		self.updateArray()