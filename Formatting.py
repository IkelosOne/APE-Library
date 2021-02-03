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
	elif checkType == "float":
		try:
			value = float(value)
			return True
		except TypeError:
			return False
		except ValueError:
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
