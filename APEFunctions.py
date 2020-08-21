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
def FindNoOfFactors(number):
    total = 1
    for x in range(1,number//2 + 1):
        if number % x == 0:
            total += 1
    return total

def FindFactors(n,prime = False):
	"""Will return an array of the prime factors in n. If prime is set to true, it will return the prime factor the amount of times it goes into n."""

	n = int(n)
	factors = []
	for x in range(1, n//2 + 1):
		if n % x == 0:
			if prime:
				if IsPrime3(x):
					for i in range(n//x):
						factors.append(x)
			else:
				factors.append(x)
	return factors

def LowestCommonMultiple(n, m):
	"""Will return the lowest common multiple of the two inputs"""

	n = int(n)
	m = int(m)
	nMultiples = []
	mMultiples = []
	count = -1
	while 0 == 0:
		count += 1
		nMultiples.append(n*(count+1))
		mMultiples.append(m * (count+1))
		if nMultiples[count] > mMultiples[count]: #  Allows for catchup (stop checking when multiples are far apart maybe idk what I'm doing tbh but it works so it's all good right? I'm gonna listen to some Muse now)
			for x in range(len(nMultiples)):
				if mMultiples[count] == nMultiples[x]:
					return nMultiples[x]
		else:
			for y in range(len(mMultiples)):
				if nMultiples[count] == mMultiples[y]:
					return mMultiples[y]

def LowestCommonMultipleWIP(n,m):
	"""Will use prime factors to calculate lcm more efficiently for large inputs"""

	n = int(n)
	m = int(m)
	if IsPrime3(n) or IsPrime3(m):
		return n*m
	else:
		pass #  Use an upcoming function to get the factors of each of the numbers
		nFacList = FindFactors(n,True)
		mFacList = FindFactors(m,True)
		combinedFacList = []
		for x in range(len(nFacList)): #  Attempts to create list of common prime factors, the most amount of times they occur
			for y in range(len(mFacList)):
				try:
					if mFacList[x] == nFacList[y]:
						commonFactor = mFacList[x]
						if OccurencesInList(commonFactor,mFacList) > OccurencesInList(commonFactor,nFacList):
							for i in range(OccurencesInList(commonFactor,mFacList)):
								combinedFacList.append(commonFactor)
						else:
							for i in range(OccurencesInList(commonFactor,nFacList)):
								combinedFacList.append(commonFactor)
				except IndexError:
					pass
		lcm = 1
		for t in range(len(combinedFacList)):
			lcm *= combinedFacList[t]
		return lcm

if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""
	print(LowestCommonMultiple(input(""),input("")))
	None
