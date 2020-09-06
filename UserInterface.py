#-------------------------------------------------------------------------------
# Name:        Conversion
# Purpose:	   To have all APE Library funcions for converting from format to another

import sys
sys.path.append("S:\Documents\GitHub\APE-Library")
import APEFunctions

def IntToWord(integer, mode = "Standard"):
	unitsDict = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
	tensDict = {10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
	teensDict = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}

	integer = str(integer)
	integer = int(integer)
	integer = str(integer)  # Gets rid of 0's at start of number
	word = ""
	# Starts from left side and appends on right
	if len(integer) > 12:
		if integer[-13] != "0":
			word += IntToWord(integer[:-12]) + "Trillion"
	if len(integer) > 9:
		if integer[-10] != "0":
			word += IntToWord(integer[-12:-9]) + "Billion"
	if len(integer) > 6:
		if integer[-5] != "0":
			word += IntToWord(integer[-9:-6]) + "Million"
	if len(integer) > 3:
		if integer[-4] != "0":
			word += IntToWord(integer[-6:-3]) + "Thousand"
	if len(integer) > 2:
		if integer[-3] != "0":
			word += unitsDict[int(integer[-3:-2])] + "Hundred"
	if len(integer) > 1:
		if len(integer) > 2:  # Adds and inbetween hundreds and tens value
			if integer[-2:] != "00":
				word += "And"
		if integer[-2:-1] != "1":
			if integer[-2:-1] != "0":  # stops *00 being recognised as tens
				word += tensDict[int(integer[-2:-1])*10]
		else:  # Teens
			word += teensDict[int(integer[-2:])]
	if len(integer) > 0:
		if len(integer) == 1:
			if integer[0] == "0":
				return "Zero"
			word += unitsDict[int(integer[-1:])]
		elif integer[-2] != "1":
			word += unitsDict[int(integer[-1:])]

	if mode == "language":
		return SpaceWords(word)
	return word

def SpaceWords(string):
	"""Takes a string consisting of non-spaced but capitalised words and returns the string with spaces, taking away capital letters"""
	newString = string[0].lower()
	for x in range(1,len(string)):
		if string[x].isupper():
			newString += " "+string[x].lower()
		else:
			newString += string[x]
	return newString


def GetLongestInArray(array):
	"""Returns the longest (in length) item from a one/two dimensional array"""

	width = len(array)
	try:
		height = len(array[0])
		oneDim = False
	except TypeError:
		height = 1
		oneDim = True

	longest = ""
	for x in range(width):
		if height != 1:
			for y in range(height):
				if len(str(array[x][y])) > len(longest):
					longest = str(array[x][y])
		elif len(str(array[x])) > len(longest):
				longest = str(array[x])
	return longest

def PrintArray(array):
	width = len(array)
	try:
		height = len(array[0])
		oneDim = False
	except TypeError:
		height = 1
		oneDim = True

	horizontalBoarder = "-"
	verticalBoarder = "¦"

	# Calcultes horizontal boarder length
	row = horizontalBoarder
	longest = len(GetLongestInArray(array))
	for x in range((longest+1) * width):  # Adds horizontal boarder for every row
		row += horizontalBoarder
	#row += horizontalBoarder
	horizontalBoarder = row

	for y in range(height):
		print(horizontalBoarder)
		row = ""
		for x in range(width):  # Adds in the row of the array
			if oneDim == False:
				row += verticalBoarder + str(array[x][y])
				for gap in range(len(str(array[x][y])),longest):
					row += " "
			else:
				row += verticalBoarder + str(array[x])
				for gap in range(len(str(array[x])),longest):
					row += " "

		row += verticalBoarder
		print(row)
	print(horizontalBoarder)


if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""
	PrintArray([342,865,234])
	print(PrintArray([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]))