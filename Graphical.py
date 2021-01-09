import turtle

screenWidth =  1600
screenHeight = 900
marginWidth = 20
marginHeight = 20

def plotGraph(array): # Imported from terrain gen
	try:
		screen = turtle.Screen()


		screen.setup(screenWidth,screenHeight)
		pen = turtle.Turtle()
		pen.up()
		pen.goto((-screenWidth/2) + marginWidth,(-screenHeight/2) + marginHeight)
		pen.down()
		for x in range(len(array)):
			coords = convertCoordsToStandard(x*10,int(array[x])*10)
			pen.goto(coords[0],coords[1])
		pen.up()
		screen.mainloop()
	except TypeError:
		pass

def convertCoordsToStandard(xCoord,yCoord):
	global screenWidth
	global screenHeight
	global marginWidth
	global marginHeight

	coords = [(-screenWidth/2) + marginWidth + xCoord,(-screenHeight/2) + marginHeight + yCoord]
	return coords

plotGraph([0,1,2,1,3])