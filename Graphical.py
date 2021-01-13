import turtle
import time
import StandardFunctions
import re # For regex

screenWidth =  1600
screenHeight = 900

marginWidth = 20
marginHeight = 20

originScreenCoords = [100,100]

def plotGraph(array): # Imported from terrain gen
	t0 = time.time()

	screen = turtle.Screen()
	turtle.tracer(0,0)

	dataRange = getMaxValue(array)-getMinValue(array)

	gapWidth = (screenWidth-marginWidth-originScreenCoords[1])/len(array)
	unitHeight = (screenHeight-marginHeight)/dataRange

	screen.setup(screenWidth,screenHeight)
	terry = turtle.Turtle()
	terry.speed = 0
	terry.up()
	terry.goto(convertCoords(0,0))
	terry.down()
	for x in range(len(array)):
		coords = convertCoords(x*gapWidth,int(array[x])*unitHeight,array)
		terry.goto(coords[0],coords[1])
	terry.up()
	turtle.update()

	t1 = time.time()
	print("Time required:", t1 - t0)
	screen.mainloop()


def convertCoords(xCoord,yCoord,array = [0]):
	# Starts the coords 0,0 from bottom left, taking into account the given global margin variables
	# Will add an option to let 0,0 be the center as this will be useful
	global screenWidth
	global screenHeight
	global marginWidth
	global marginHeight
	global originScreenCoords


	coords = [(-screenWidth/2) + marginWidth + originScreenCoords[0] + xCoord,(-screenHeight/2) + marginHeight + originScreenCoords[1] + yCoord]
	return coords

def setOriginPosition(position):
	global originScreenCoords
	if position=="center":
		originScreenCoords=[screenWidth/2,screenHeight/2]
	elif position=="bottomLeft":
		originScreenCoords=[0,0]

def getMaxValue(array):
	# Gets maximum value in array
	max = array[0]
	for i in range(len(array)):
		if array[i]>max:
			max = array[i]
	return max

def getMinValue(array):
	# Gets minimum value in array
	min = array[0]
	for i in range(len(array)):
		if array[i]<min:
			min = array[i]
	return min

def equationToArray(formulaString,resolution,min=0,max=(screenWidth-marginWidth)):
	# Eventually you will be able to enter an equation in the form y=.x..
	# The resolution is how many points are plotted on the graph. A resolution of 1 means one straight line, 2 means two lines etc.
	# (A resolution of at least 20 is recommended)
	array = []
	#gapWidth = (screenWidth-marginWidth)/(screenWidth/resolution) # This is what was used when the x axis was a fixed scale, 0 to screenWidth
	graphRange = max - min
	gapWidth = graphRange/resolution
	for i in range(round(resolution)):
		x = min + gapWidth*i
		equationString = re.sub("x",str(x),formulaString)
		answer = calculateFromString(equationString)
		array.append(answer)
	return array



def calculateFromString(equationString):
	"""Takes an equation as a string containing only real numbers and basic operators. Brackets not yet supported"""
	#parts = equationString.split("(\+|-)") # Splits at + or - but keeps the operator a the beginning of each item
	parts = re.split("(\+|-)",equationString)
	firstOp = []
	secondOp = []
	for i in range(len(parts)):
		if parts[i] == "+" or parts[i] == "-":
			secondOp.append(parts[i])
		else:
			currentFirstOp = parts[i]
			if currentFirstOp.find("*")!=-1:
				currentFirstOp = currentFirstOp.split("*")
				if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
					firstOp.append(-float(currentFirstOp[0])*float(currentFirstOp[1]))
					secondOp[len(secondOp)-1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0])*float(currentFirstOp[1]))
			elif currentFirstOp.find("^")!=-1:
				currentFirstOp = currentFirstOp.split("^")
				if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
					firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
					secondOp[len(secondOp)-1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
			elif currentFirstOp.find("/")!=-1:
				currentFirstOp = currentFirstOp.split("/")
				if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
					firstOp.append(-float(currentFirstOp[0])/float(currentFirstOp[1]))
					secondOp[len(secondOp)-1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0])/float(currentFirstOp[1]))
			else:
				#print("No primary operation found in "+currentFirstOp)
				try:
					firstOp.append(float(currentFirstOp))
				except ValueError:
					firstOp.append(0)

	answer = firstOp[0]
	for o in range(1,len(firstOp)):

		if secondOp[o-1] == "+":
			answer += firstOp[o]
		elif secondOp[o-1] == "-":
			answer -= firstOp[o]
		else:
			print("Can't understand this "+secondOp+" operator yet")

	#print(answer)
	return answer


if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""


	#plotGraph([0,1,2,1,3,4,5,3,2])
	#setOriginPosition("center")
	setOriginPosition("bottomLeft")
	plotGraph(equationToArray("x^2",11,-5,5))
	#print(calculateFromString("3*4+6/3-10/2"))

	None
