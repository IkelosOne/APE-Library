import re
import StandardFunctions
import math

<<<<<<< Updated upstream

def calculateFromString(equationString):
	"""Uses reccursion to break down an equation to its smallest calculations"""
=======
def calculateFromStringObsolete(equationString):
	"""Takes an equation as a string containing only real numbers and basic operators. Brackets not yet supported"""

	#parts = equationString.split("(\+|-)") # Splits at + or - but keeps the operator a the beginning of each item
	parts = re.split("(\+|\()", equationString)
	firstOp = []
	secondOp = []
	for i in range(len(parts)):
		if parts[i] == "+":
			secondOp.append(parts[i])
		else:
			currentFirstOp = parts[i]
			if currentFirstOp.find("*") != -1:
				currentFirstOp = currentFirstOp.split("*")
				if len(secondOp) > 0 and secondOp[len(secondOp) - 1] == "-":
					firstOp.append(-float(currentFirstOp[0]) * float(currentFirstOp[1]))
					secondOp[len(secondOp) - 1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0]) * float(currentFirstOp[1]))
			elif currentFirstOp.find("^") != -1:
				currentFirstOp = currentFirstOp.split("^")
				if len(secondOp) > 0 and secondOp[len(secondOp) - 1] == "-":
					firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
					secondOp[len(secondOp) - 1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
			elif currentFirstOp.find("/") != -1:
				currentFirstOp = currentFirstOp.split("/")
				if len(secondOp) > 0 and secondOp[len(secondOp) - 1] == "-":
					firstOp.append(-float(currentFirstOp[0]) / float(currentFirstOp[1]))
					secondOp[len(secondOp) - 1] = "+"
				else:
					firstOp.append(float(currentFirstOp[0]) / float(currentFirstOp[1]))
			else:
				#print("No primary operation found in "+currentFirstOp)
				try:
					firstOp.append(float(currentFirstOp))
				except ValueError:
					firstOp.append(0)

	answer = firstOp[0]
	for o in range(1, len(firstOp)):

		if secondOp[o - 1] == "+":
			answer += firstOp[o]
		elif secondOp[o - 1] == "-":
			answer -= firstOp[o]
		else:
			print("Can't understand this " + secondOp + " operator yet")

	#print(answer)
	return answer

def calculateFromString(equationString):
	"""uses reccursion to break down an equation to its smallest calculations"""

>>>>>>> Stashed changes
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

		if equationString[x] == "(":
			for i in range(x, len(equationString)):
				if equationString[i] == ")":
<<<<<<< Updated upstream
					numberList.append(calculateFromString(equationString[x+1:i])) # Will send whats inside the bracket to get processed
=======
					numberList.append(calculateFromString2(equationString[x + 1:i]))  # Will send whats inside the bracket to get processed
>>>>>>> Stashed changes
					break
			x = i  # Stops doing everything else in the bracket as it will be done in the reccursion
		elif equationString[x] == "+" or equationString[x] == "-" or equationString[x] == "*" or equationString[x] == "/" or equationString[x] == "^":
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
		elif StandardFunctions.isType(equationString[x], "int") == True:
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

		x += 1

	answer = numberList[0]
	for n in range(len(operatorList)):
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
				answer = math.pow(answer, numberList[n + 1])  # This can throw errors and not do stupid ocmplex numbers
			except ValueError:
				answer = -((-answer)**(numberList[n + 1]))  # Cheating?
	return answer




def binaryToDecimal(binary):
	binary = str(binary)
	digits = len(binary)
	decimal = 0
	for x in range(digits):
		if x == digits-1: # 0^0 = 1 according to python so had to manually fix this
			decimal += int(binary[x])
		else:
			decimal += (int(binary[x])*2)**(digits-x-1)
	return decimal



if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""

<<<<<<< Updated upstream
	#print(calculateFromString("2+(3-(5*4))"))
	print(binaryToDecimal(10010111))

	None
=======
	None
>>>>>>> Stashed changes
