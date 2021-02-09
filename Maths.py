import re
import StandardFunctions
import Formatting
import math


def calculateFromString(equationString):
	"""Uses reccursion to break down an equation to its smallest calculations"""

	numberList = []
	operatorList = []
	x = 0
	while x < len(equationString):
		try:
			if equationString[x] == equationString[x + 1]:  # Gets rid of double + and double - when encountered
				if equationString[x] == "+" or equationString[x] == "-":
					equationString = equationString[0:x] + "+" + equationString[x + 2:]
		except IndexError:
			pass

		if equationString[x] == "(": # Deals with pesky brackets
			for i in range(x, len(equationString)):
				if equationString[i] == ")":
					numberList.append(calculateFromString2(equationString[x + 1:i]))  # Will send whats inside the bracket to get processed
					break
			x = i  # Stops doing everything else in the bracket as it will be done in the reccursion
		elif equationString[x] == "+" or equationString[x] == "-" or equationString[x] == "*" or equationString[x] == "/" or equationString[x] == "^": # Deals with pesky operators (minus is the worst)
			if (equationString[x] == "-" and x == 0) or (equationString[x] == "-" and (equationString[x - 1] == "+" or equationString[x] == "*" or equationString[x] == "/" or equationString[x] == "^")):  # Handles negative numbers
				for i in range(x + 1, len(equationString)):
					if StandardFunctions.isType(equationString[i], "int") == False and equationString[i] != ".":  # Keeps going until the number ends and there is an operator
						try:
							numberList.append(float(equationString[x:i]))
							x = i - 1
						except ValueError:
							numberList.append(float(equationString[x]))
						break
			else:
				operatorList.append(equationString[x])
		elif StandardFunctions.isType(equationString[x], "int") == True: # Yay, actual, easy-to-understand, numbers!
			for i in range(x, len(equationString) + 1):
				if i > len(equationString) - 1:  # Checks if this is the last digit in equationString
					numberList.append(float(equationString[x:i]))
					x = i - 1
					break
				elif StandardFunctions.isType(equationString[i], "int") == False and equationString[i] != ".":  # Keeps going until the number ends and there is an operator
					try:
						numberList.append(float(equationString[x:i]))
						x = i - 1
					except ValueError:
						numberList.append(float(equationString[x]))
					break

		x += 1 # Doesn't use for loop because some segments get skipped over in one loop cycle so x increment is not consistent

	answer = numberList[0] # Final compiler
	for n in range(len(operatorList)): # Performs operations to all the numbers in chromatic order (BIDMAS rules don't apply yet)
		if operatorList[n] == "+":
			answer += numberList[n + 1]
		elif operatorList[n] == "-":
			answer -= numberList[n + 1]
		elif operatorList[n] == "*":
			answer *= numberList[n + 1]
		elif operatorList[n] == "/":
			answer /= numberList[n + 1]
		elif operatorList[n] == "^":
			try:
				#answer = answer**(numberList[n+1])
				answer = math.pow(answer, numberList[n + 1])  # This can throw errors and not do stupid complex numbers
			except ValueError:
				answer = -((-answer)**(numberList[n + 1]))  # Cheating? Makes it not negative, then makes it negative afterwards
	return answer



def toDecimal(number,base):
	"""This function is so incredibly based"""
	number = str(number)
	digits = len(number)
	decimal = 0
	for x in range(digits):
		digit = number[x]
		if Formatting.isType(digit,"string"):
			digit = ord(digit.upper()) -65+10 # Allows use of letters to represent numbers above 9
		if x == digits-1: # 0^0 = 1 according to python so had to manually fix this
			decimal += int(digit)
		else:
			decimal += (int(digit)*base)**(digits-x-1)
	return decimal


def decimalToBinary(decimal):
	decimal = int(decimal)
	binary = ""

	remaing = decimal

	if decimal == 0:
		return 0
	elif decimal == 1:
		return 1
	binDigits = round(math.log2(decimal)+0.5) # Rounds up to find the numebr of digits
	for x in range(binDigits):
		i = binDigits-x-1
		if 2**(i) <= remaing:
			binary += "1"
			remaing -= 2**i
		else:
			binary += "0"


	return binary



if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""

	#print(calculateFromString("2+(3-(5*4))"))
	for x in range(20):
		print(decimalToBinary(x+1))

	None