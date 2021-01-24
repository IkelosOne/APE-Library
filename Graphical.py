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

def plotGraph(equationArray): # Imported from terrain gen
	t0 = time.time()

	screen = turtle.Screen()
	turtle.tracer(0,0)

	array = equationArray.get_array()
	dataRange = StandardFunctions.getMaxValue(array)-StandardFunctions.getMinValue(array)

	gapWidth = (screenWidth-marginWidth-originScreenCoords[1])/len(array)
	unitHeight = (screenHeight-marginHeight)/dataRange

	screen.setup(screenWidth,screenHeight)
	terry = turtle.Turtle()
	terry.speed = 0
	terry.up()

	# Draws X axis
	print(equationArray.get_startX())
	print(equationArray.get_endX())
	terry.goto(convertCoords(equationArray.get_startX()*gapWidth,0))
	terry.down()
	terry.goto(convertCoords(equationArray.get_endX()*gapWidth,0))
	terry.up()

	# Draws Y axis
	print(StandardFunctions.getMinValue(array))
	print(StandardFunctions.getMaxValue(array))
	terry.goto(convertCoords(0,StandardFunctions.getMinValue(array)*unitHeight))
	terry.down()
	terry.goto(convertCoords(0,StandardFunctions.getMaxValue(array)*unitHeight))
	terry.up()

	terry.goto(convertCoords(0,0))
	for x in range(len(array)):
		coords = convertCoords(x*gapWidth,int(array[x])*unitHeight)
		terry.goto(coords[0],coords[1])
		terry.down()
	terry.up()
	turtle.update()

	t1 = time.time()
	print("Time required:", t1 - t0)
	screen.mainloop()


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




if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""


	equationObject = EquationArray.EquationArray("x^3+x^2-3*x",-5,50)
	plotGraph(equationObject)

	None
