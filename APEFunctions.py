def IsPrime(n):  # Version 2 (will be replaced with version 3 once developent on it ends as bugs may occur)
	"""Input n, returns True if n is prime and False if not."""

	n = int(n)
	if n > 1:
		x = 2
		while x * x <= n:  # x * x < n is much more efficient than x < sqrt(n)
			if (n % x) == 0:
				return False
			x += 1
		return True
	else:
		return False

def IsPrime3(n):  # Version 3 - Time 16.04
	"""Input n, returns True if n is prime and False if not."""

	n = int(n)
	if n > 1:
		x = 2
		while x * x <= n:  # x*x<n is much more efficient than x<sqrt(n)
			if (n % x) == 0:
				return False
			x += 2
		return True
	else:
		return False

def InsertCommas(number):
	"""Inserts commas into the corresponding places in a number."""

	string = str(number)
	newString = string
	commasNeeded = len(str(number)[:-1]) // 3
	while commasNeeded > 0:
		newString = newString[:-(3 * commasNeeded)] + "," + newString[-(3 * commasNeeded):]
		commasNeeded -= 1
	return newString

def IsPalindromic(n):
	"""Returns True if n is palindromic and False if not."""

	n = str(n)
	for x in range(len(n) // 2):
		if n[x] != n[len(n) - x - 1]:
			return False
	return True

def OccurencesInList(item, list1):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo !!! DOES IT? - Arun
	"""Returns the amount of occurences of an item in a list."""

	count = 0
	for x in range(len(list1)):
		if list1[x] == item:
			count += 1
	return count

def NextCollatzTerm(number):
	"""Will return the next number in the collatz sequence"""

	if number % 2 == 0:
		number /= 2
	else:
		number *= 3
		number += 1
	return number

def CollatzSequencer(start):
	"""Starts with "start" number then follows collatz sequence to 1 and returns list for sequence"""

	result = int(start)
	resultsList = []
	while result != 1:
		result = NextCollatzTerm(result)
		resultsList.append(int(result))
	return resultsList

def HighestCollatzTerm(start):
	"""Starts with "start" number then follows collatz sequence to 1 and returns the highest number in the sequence"""

	result = int(start)
	largest = 0
	while result != 1:
		result = NextCollatzTerm(result)
		if result > largest:
			largest = result
	return int(largest)

def TriangulerSequencer(sequenceLength=0, term=0):
	"""Sequence: Generates sequence up to "sequenceLength" and returns list for sequence """
	"""Term: Generates sequence to find "term", which is then returned"""  # WIP #https://www.mathsisfun.com/algebra/triangular-numbers.html

	sequenceLength = int(sequenceLength)
	term = int(term)
	sequence = [1, 1]
	if term > 0:
		sequenceLength = term
	elif sequenceLength == 0:  # Error mesage WIP
		term = 0 / 0
		print("Sequence length or term must be inputted")
		return 0
	for x in range(1, sequenceLength):
		sequence.append(sequence[x - 1] + sequence[x])
	if term > 0:
		return sequence[term]
	else:
		return sequence[1:]  # Doesn't return the first 1


##--------------------------------------------------------------------------------------
def TestForLychrel(number,attempts = 0):
	"""Will return true if a lychrel, false if not (Will test 50 times)"""

	number = int(number)
	result = number + int(str(number)[::-1])
	#print(number)
	if IsPalindromic(result):
		return False
	else:
		if attempts < 50:
			return TestForLychrel(result,attempts+1) #Could get messy
		else:
			return True
##--------------------------------------------------------------------------------------
def Factorial(n):
	"""Will return the factorial of n"""

	product = 1
	for x in range(1,int(n)+1):
		product *= x
	return product
##--------------------------------------------------------------------------------------

if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""
	print(Factorial(input("")))
	None
