import turtle

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
	pen.up()
	pen.goto((-screenWidth/2) + marginWidth,(-screenHeight/2) + marginHeight)
	pen.down()
	for x in range(len(array)):
		coords = convertCoords(x*gapWidth,int(array[x])*unitHeight)
		pen.goto(coords[0],coords[1])
	pen.up()
	screen.mainloop()

def convertCoords(xCoord,yCoord):
	global screenWidth
	global screenHeight
	global marginWidth
	global marginHeight

	coords = [(-screenWidth/2) + marginWidth + xCoord,(-screenHeight/2) + marginHeight + yCoord]
	return coords

def getMaxValue(array):
	max = array[0]
	for i in range(len(array)):
		if array[i]>max:
			max = array[i]
	return max

def getMinValue(array):
	min = array[0]
	for i in range(len(array)):
		if array[i]<min:
			min = array[i]
	return min

plotGraph([0,1,2,1,3])