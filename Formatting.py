def is_bracket_balanced():
	"""Takes a number of lines of code and validates the number of opened and closed brackets.
	This is the program I said I made with that uni student years ago...
	When you were boasting about how clever you were? xd Also this will be very useful for the
	calculator.

	rtype: bool"""

	a = int(input("How many lines would you like to check?\n"))
	for x in range(a):
		var = input("Enter variable:\n")
		brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
		bracketCount = {"(": 0, "[": 0, "{": 0, "<": 0}
		for i in range(len(var)):
			if var[i] in list(brackets.keys()):
				bracketCount[brackets[var[i]]] -= 1
				#print("-1 from", var[i])
			elif var[i] in list(brackets.values()):
				bracketCount[var[i]] += 1
				#print("+1 from", var[i])

	if sum(bracketCount.values()) == 0 and -1 not in list(bracketCount.values()):
		return True
	else:
		return False

def GetInteger(inputMin, inputMax, inputMessage):
	"""Called when integer input is required, checks input according to parameters.

	This is really old, outdated, likely doesn't work, but was an idea I had lurking in my old drive."""

	inputPass = False
	while inputPass is False:
		try:
			x = int(input(inputMessage))
			if x >= inputMin and x <= inputMax:
				inputPass = True
				return x
			else:
				print("Error: Input must be integer between", inputMin, "and", str(inputMax) + ".")
		except ValueError:
			print("Error: Input must be integer between", inputMin, "and", str(inputMax) + ".")

def GetFloat(inputMin, inputMax, inputMessage):
	"""Called when float input is required, checks input according to parameters.

	This is really old, outdated, likely doesn't work, but was an idea I had lurking in my old drive."""

	inputPass = False
	while inputPass is False:
		try:
			x = float(input(inputMessage))
			if x >= inputMin and x <= inputMax:
				inputPass = True
				return x
			else:
				print("Error: Input must be float between", inputMin, "and", str(inputMax) + ".")
		except ValueError:
			print("Error: Input must be float between", inputMin, "and", str(inputMax) + ".")

def InsertCommas(number):
	"""Inserts commas into the corresponding places in a number."""

	string = str(number)
	newString = string
	commasNeeded = len(str(number)[:-1]) // 3
	while commasNeeded > 0:
		newString = newString[:-(3 * commasNeeded)] + "," + newString[-(3 * commasNeeded):]
		commasNeeded -= 1
	return newString

#Note: I think it's easier to write if type(a) == b than to call this function... Consider moving to obsolete.
def isType(value, checkType):

	if checkType == "int":
		try:
			value = int(value)
			return True
		except TypeError:
			return False
		except ValueError:
			return False
	elif checkType == "float" or checkType == "string":
		try:
			value = float(value)
			if checkType == "float":
				return True
			else:
				return False
		except TypeError:
			if checkType == "string":
				return True
			else:
				return False
		except ValueError:
			if checkType == "string":
				return True
			else:
				return False

#Note: This is build-in: max(). Consider moving to obsolete.
def getMaxValue(array):
	# Gets maximum value in array
	max = array[0]
	for i in range(len(array)):
		try:
			if array[i] > max:
				max = array[i]
		except TypeError:
			pass
	return max

#Note: This is built-in: min(). Cosndier moving to obsolete.
def getMinValue(array):
	# Gets minimum value in array
	min = array[0]
	for i in range(len(array)):
		try:
			if array[i] < min:
				min = array[i]
		except TypeError:
			print("Complex number found and ignored")
	return min

def intAllInArray(array):
	"""Attempts to turn all data inside the array to integers"""
	try:
		for x in range(len(array)):
			array[x] = int(array[x])
		return array
	except TypeError:
		print("Cannot convert all in array to integers")
		return [0]

def arrayToString(array):
	"""Takes array and returns a string without , or []"""
	string = ""
	for x in range(len(array)):
		string += str(array[x])
	return string


# Ascii characters that are actually characters
ValToChar = {0: " ", 1: "!", 2: '"', 3: "#", 4: "$", 5: "%", 6: "&", 7: "'", 8: "(", 9: ")", 10: "*", 11: "+", 12: ",", 13: "-", 14: ".", 15: "/", 16: "0", 17: "1", 18: "2", 19: "3", 20: "4", 21: "5", 22: "6", 23: "7", 24: "8", 25: "9", 26: ":", 27: ";", 28: "<", 29: "=", 30: ">", 31: "?", 32: "@", 33: "A", 34: "B", 35: "C", 36: "D", 37: "E", 38: "F", 39: "G", 40: "H", 41: "I", 42: "J", 43: "K", 44: "L", 45: "M", 46: "N", 47: "O", 48: "P", 49: "Q", 50: "R", 51: "S", 52: "T", 53: "U", 54: "V", 55: "W", 56: "X", 57: "Y", 58: "Z", 59: "[", 60: "\\", 61: "]", 62: "^", 63: "_", 64: "`", 65: "a", 66: "b", 67: "c", 68: "d", 69: "e", 70: "f", 71: "g", 72: "h", 73: "i", 74: "j", 75: "k", 76: "l", 77: "m", 78: "n", 79: "o", 80: "p", 81: "q", 82: "r", 83: "s", 84: "t", 85: "u", 86: "v", 87: "w", 88: "x", 89: "y", 90: "z", 91: "{", 92: "|", 93: "}", 94: "~"}
CharToVal = {v: k for k, v in ValToChar.items()}
