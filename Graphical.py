import turtle
import time
import StandardFunctions
import re # For regex
import EquationArray

screenWidth =  1600
screenHeight = 900

marginWidth = 20
marginHeight = 20

originScreenCoords = [100,100]
screenCoords = [0,0]

moveSpeed = 40

screen = turtle.Screen()
screen.setup(screenWidth,screenHeight)

def plotGraph(equationArray): # Draws a graph from the given EquationArray object (regular arrays have been broken)
	global screen
	t0 = time.time()


	turtle.tracer(0,0)

	array = equationArray.get_array()
	dataRange = StandardFunctions.getMaxValue(array)-StandardFunctions.getMinValue(array)

	gapWidth = (screenWidth-marginWidth-originScreenCoords[1])/len(array)
	unitHeight = (screenHeight-marginHeight)/dataRange

	screen = turtle.Screen()
	screen.setworldcoordinates(screenCoords[0],screenCoords[1],screenWidth,screenHeight)
	#screen.setup(screenWidth,screenHeight)
	terry = turtle.Turtle()
	terry.speed = 0
	terry.up()

	# Draws X axis
	"""
	print(equationArray.get_startX())
	print(equationArray.get_endX())
	terry.goto(convertCoords(equationArray.get_startX()*gapWidth,0))
	terry.down()
	terry.goto(convertCoords(equationArray.get_endX()*gapWidth,0))
	terry.up()"""

	# Draws Y axis
	"""
	print(StandardFunctions.getMinValue(array))
	print(StandardFunctions.getMaxValue(array))
	terry.goto(convertCoords(0,StandardFunctions.getMinValue(array)*unitHeight))
	terry.down()
	terry.goto(convertCoords(0,StandardFunctions.getMaxValue(array)*unitHeight))
	terry.up()"""

	terry.goto(convertCoords(0,0))
	for x in range(len(array)):
		coords = convertCoords(x*gapWidth,int(array[x])*unitHeight)
		terry.goto(coords[0],coords[1])
		terry.down()
	terry.up()
	turtle.update()

	t1 = time.time()
	print("Time required:", t1 - t0)
	screen.onkey(moveViewUp,"Up")
	screen.onkey(moveViewDown,"Down")
	screen.onkey(moveViewLeft,"Left")
	screen.onkey(moveViewRight,"Right")
	screen.listen()
	turtle.done()
	#screen.mainloop()


def convertCoords(xCoord,yCoord):
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
	if position=="c":
		originScreenCoords=[screenWidth/2,screenHeight/2]
	elif position=="bl":
		originScreenCoords=[0,0]

def moveViewUp():
	global screen
	global moveSpeed
	print("Go up")
	screenCoords[1] += moveSpeed
	screen.setworldcoordinates(screenCoords[0],screenCoords[1],screenWidth,screenHeight)

def moveViewDown():
	global screen
	global moveSpeed
	screenCoords[1] -= moveSpeed
	screen.setworldcoordinates(screenCoords[0],screenCoords[1],screenWidth,screenHeight)

def moveViewLeft():
	global screen
	global moveSpeed
	screenCoords[0] -= moveSpeed
	screen.setworldcoordinates(screenCoords[0],screenCoords[1],screenWidth,screenHeight)

def moveViewRight():
	global screen
	global moveSpeed
	screenCoords[0] += moveSpeed
	screen.setworldcoordinates(screenCoords[0],screenCoords[1],screenWidth,screenHeight)



if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""


	equationObject = EquationArray.EquationArray("(x-2)^(1/3)",-1,2)
	equationObject.set_resolution(4)
	setOriginPosition("c")
	plotGraph(equationObject)

	None
