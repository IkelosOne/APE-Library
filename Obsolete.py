def CommaNumber(number):
	"""Takes number and adds commas every 3 digits. Returns string"""

	number = str(number)
	numList = []
	seperates = len(number) // 3
	for x in range(seperates):  # Repeats for the amount of commas
		leftLim = - (seperates + 1 - x) * 3
		rightLim = - ((seperates - x) * 3)
		numList.append(number[leftLim:rightLim])
	numList.append(number[-3:])
	result = ""
	for n in range(len(numList)):  # Turns list into string
		result = result + "," + numList[n]
	while result[0] == ",":  # Gets rid of commas at start
		result = result[1:]
	return result
##--------------------------------------------------------------------------------------
def ReverseIt(inp):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo !!! DOES IT? - Arun !!! Pablo you can do "Hello"[::-1] apparently
	"""Takes string or int and return reversed version as string."""

	inp = str(inp)
	revNum = ""
	for x in range(len(inp)):
		digit = inp[len(inp) - x - 1]
		revNum += digit
	return revNum