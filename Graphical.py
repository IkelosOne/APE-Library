import turtle


def GraphicalHeightMap(array): # Imported from terrain gen
	screen = turtle.Screen()

	screen.screensize()
	pen = turtle.Turtle()
	pen.down()
	for x in range(len(array)):
		pen.goto((x*10)-10,int(array[x])*10)
	pen.up()
	screen.mainloop()

GraphicalHeightMap([0,1,2,1,3])
#plotGraph([0,1,2,1,3])