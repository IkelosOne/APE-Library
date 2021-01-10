import turtle
import time
import APEFunctions

screenWidth =  1600
screenHeight = 900

marginWidth = 20
marginHeight = 20

def plotGraph(array): # Imported from terrain gen

	screen = turtle.Screen()

	dataRange = getMaxValue(array)-getMinValue(array)

	gapWidth = (screenWidth-marginWidth)/len(array)
	unitHeight = (screenHeight-marginHeight)/dataRange

	screen.setup(screenWidth,screenHeight)
	pen = turtle.Turtle()
	pen.speed = 0
	pen.up()
	pen.goto((-screenWidth/2) + marginWidth,(-screenHeight/2) + marginHeight)
	pen.down()
	for x in range(len(array)):
		coords = convertCoords(x*gapWidth,int(array[x])*unitHeight)
		pen.goto(coords[0],coords[1])
	pen.up()
	screen.mainloop()

def convertCoords(xCoord,yCoord):
	# Starts the coords 0,0 from bottom left, taking into account the given global margin variables
	# Will add an option to let 0,0 be the center as this will be useful
	global screenWidth
	global screenHeight
	global marginWidth
	global marginHeight

	coords = [(-screenWidth/2) + marginWidth + xCoord,(-screenHeight/2) + marginHeight + yCoord]
	return coords

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

def equationToArray(equationString,resolution):
	# Eventually you will be able to enter an equation in the form y=x...
	# The resolution is how many points are plotted on the graph. A resolution of 1 means one straight line, 2 means two lines etc.
	# (A resolution of at least 20 is recommended)
	print("Ahhhhherrrr I'll do this tomorrow")
	array = [resolution**2+resolution*3+2]
	gapWidth = (screenWidth-marginWidth)/(screenWidth/resolution)
	for i in range(round(resolution)):
		#array.append((resolution*i*screenWidth)**3+2*(resolution*i*screenWidth)**2+1/2*(resolution*i*screenWidth)+2)
		#array.append(1000/(resolution*i*screenWidth+2))
		x = gapWidth*i
		array.append(x**2 + 3*x + 4)
	return array

if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""


	t0 = time.time()


	#plotGraph([0,1,2,1,3,4,5,3,2])
	plotGraph(equationToArray("x",20))


	t1 = time.time()
	print("Time required:", t1 - t0)

	None
