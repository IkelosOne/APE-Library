import time

def IsPrime(n):
	"""Input n, returns True if n is prime and False if not.
	Version 3 - Time 15.81"""

	if n > 2:
		if n % 2 == 0:
			return False
		x = 3
		while x * x <= n:  # x*x<n is much more efficient than x<sqrt(n)
			if (n % x) == 0:
				return False
			x += 2  # Only cycles through odd numbers
		return True
	else:
		if n == 2:
			return True
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
	"""Starts with "start" number then follows collatz sequence to 1 and returns the highest number
	in the sequence"""

	result = int(start)
	largest = 0
	while result != 1:
		result = NextCollatzTerm(result)
		if result > largest:
			largest = result
	return int(largest)

def TriangulerSequencer(sequenceLength=0, term=0):
	"""Sequence: Generates sequence up to "sequenceLength" and returns list for sequence
	Term: Generates sequence to find "term", which is then returned

	WIP
	Source: https://www.mathsisfun.com/algebra/triangular-numbers.html"""

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

def TestForLychrel(number, attempts=0):
	"""Will return true if a lychrel, false if not (Will test 50 times)"""

	number = int(number)
	result = number + int(str(number)[::-1])
	#print(number)
	if IsPalindromic(result):
		return False
	else:
		if attempts < 50:
			return TestForLychrel(result, attempts + 1)  # Could get messy
		else:
			return True

def Factorial(n):
	"""Will return the factorial of n"""

	product = 1
	for x in range(1, int(n) + 1):
		product *= x
	return product

def FindNoOfFactors(number):
	total = 1
	for x in range(1, number // 2 + 1):
		if number % x == 0:
			total += 1
	return total

def FindFactors(n):
	"""Will return an array of the prime factors in n. If prime is set to true, it will return the
	prime factor the amount of times it goes into n."""

	n = int(n)
	factors = []
	for x in range(1, n // 2 + 1):
		if n % x == 0:
			factors.append(x)
	return factors

def FindPrimeFactors(n):
	"""Will return a list of the prime factors, repeated as many times as to produce n"""

	pFactors = []
	for x in range(2, n // 2 + 1):
		if n % x == 0:
			if IsPrime(x):
				pFactors.append(x)
				if IsPrime(n // x):
					pFactors.append(n // x)
				else:
					reccursive = FindPrimeFactors(n // x)
					for i in range(len(reccursive)):
						pFactors.append(reccursive[i])
			else:
				reccursive = FindPrimeFactors(n // x)
				for i in range(len(reccursive)):
					pFactors.append(reccursive[i])
			return pFactors

def LowestCommonMultiple(n, m):
	"""Will return the lowest common multiple of the two inputs
	Time - > 2 hours"""

	n = int(n)
	m = int(m)
	nMultiples = []
	mMultiples = []
	count = -1
	while 0 == 0:
		count += 1
		nMultiples.append(n * (count + 1))
		mMultiples.append(m * (count + 1))
		if nMultiples[count] > mMultiples[count]:  # Allows for catchup (stop checking when multiples are far apart maybe idk what I'm doing tbh but it works so it's all good right? I'm gonna listen to some Muse now)
			for x in range(len(nMultiples)):
				if mMultiples[count] == nMultiples[x]:
					return nMultiples[x]
		else:
			for y in range(len(mMultiples)):
				if nMultiples[count] == mMultiples[y]:
					return mMultiples[y]

def LowestCommonMultiple2(n, m):  # Good to test with 12345678911111111111,98765432199999999999
	"""Will use prime factors to calculate lcm more efficiently for large inputs
	Version 2 - Time: 59.431"""

	n = int(n)
	m = int(m)
	if n % m == 0:  # Checks some shortcut methods first
		return n
	elif m % n == 0:
		return m
	elif IsPrime(n) or IsPrime(m):
		return n * m
	else:
		pass  # Use an upcoming function to get the factors of each of the numbers
		nFacList = FindPrimeFactors(n)
		mFacList = FindPrimeFactors(m)
		factors = []
		factor = 1
		for x in range(len(nFacList)):  # Attempts to create list of common prime factors, the most amount of times they occur
			for y in range(len(mFacList)):
				factor = mFacList[x]
				mOccurences = mFacList.count(factor)
				nOccurences = nFacList.count(factor)
				if nFacList[x] == mFacList[y] and factors.count(factor) == 0:  # Common factors
					if mOccurences > nOccurences:  # Will append the for most occurences
						for i in range(mOccurences):
							factors.append(factor)
					else:
						for i in range(nOccurences):
							factors.append(factor)
				else:  # Factors of only one number
					factor = mFacList[y]
					if factors.count(factor) == 0:  # Checks it's not already in list
						for i in range(mFacList.count(factor)):  # Adds new uncommon factor to list
							factors.append(factor)
					factor = nFacList[x]
					if factors.count(factor) == 0:  # Checks it's not already in list
						for i in range(nFacList.count(factor)):  # Adds new uncommon factor to list
							factors.append(factor)

		lcm = 1
		for t in range(len(factors)):
			if factors != 0:
				lcm *= factors[t]
		return lcm

def LowestCommonMultiple3(numList):  # Good to test with [12345678911111111111,98765432199999999999]
	"""Takes a list of any length and will use prime factors to calculate lcm more efficiently for large inputs
	Version 3 - Time: 59.431"""

	if len(numList) == 1:
		return numList
	n = int(numList[0])
	m = int(numList[1])
	if n % m == 0:  # Checks some shortcut methods first
		return LowestCommonMultiple2([n]+numList[2:])
	elif m % n == 0:
		return LowestCommonMultiple2([m]+numList[2:])
	elif IsPrime(n) or IsPrime(m):
		return LowestCommonMultiple2([n * m]+numList[2:])
	else:
		pass  # Use an upcoming function to get the factors of each of the numbers
		nFacList = FindPrimeFactors(n)
		mFacList = FindPrimeFactors(m)
		factors = []
		factor = 1
		for x in range(len(nFacList)):  # Attempts to create list of common prime factors, the most amount of times they occur
			for y in range(len(mFacList)):
				factor = nFacList[x]
				mOccurences = mFacList.count(factor)
				nOccurences = nFacList.count(factor)
				if nFacList[x] == mFacList[y] and factors.count(factor) == 0:  # Common factors
					if mOccurences > nOccurences:  # Will append the for most occurences
						for i in range(mOccurences):
							factors.append(factor)
					else:
						for i in range(nOccurences):
							factors.append(factor)
				else:  # Factors of only one number
					factor = mFacList[y]
					if factors.count(factor) == 0:  # Checks it's not already in list
						for i in range(mFacList.count(factor)):  # Adds new uncommon factor to list
							factors.append(factor)
					factor = nFacList[x]
					if factors.count(factor) == 0:  # Checks it's not already in list
						for i in range(nFacList.count(factor)):  # Adds new uncommon factor to list
							factors.append(factor)

		lcm = 1
		for t in range(len(factors)):
			if factors != 0:
				lcm *= factors[t]
		return int(LowestCommonMultiple2([lcm]+numList[2:]))

if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""


	t0 = time.time()
	print(LowestCommonMultiple(12345678911111111111,98765432199999999999))
	t1 = time.time()
	print("Time required:", t1 - t0)

	None
