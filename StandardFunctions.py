def BaseConverter(x, n, m):
	"""Takes a number x in base n and returns it in base m.

	N.B. Yeah it doesn't work..."""

	return x % n // m + x % n % m

def IsPrime(n):
	"""Input n, returns True if n is prime and False if not.
	Version 3 - Time 15.81"""

	n = int(n)
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

def TriangularSequencer(sequenceLength):
	"""Sequence: Generates sequence up to "sequenceLength" and returns list for sequence"""

	sequenceLength = int(sequenceLength)
	sequence = [1]
	for x in range(0, sequenceLength):
		sequence.append(sequence[x] + x + 2)
	return sequence

def TriangleNumber(term):
	"""Term: Generates sequence to find "term", which is then returned
	WIP - Can be improved probably:
	Source: https://www.mathsisfun.com/algebra/triangular-numbers.html"""

	term = int(term)
	lastDigit = 1
	for x in range(0, term):
		lastDigit = (lastDigit + x + 2)
	return lastDigit

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
	"""Will return an array of factors in n"""

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

	if len(numList) == 1:  # Ends recursion
		return numList
	n = int(numList[0])
	m = int(numList[1])
	if n % m == 0:  # Checks some shortcut methods first
		return LowestCommonMultiple2([n] + numList[2:])
	elif m % n == 0:
		return LowestCommonMultiple2([m] + numList[2:])
	elif IsPrime(n) or IsPrime(m):
		return LowestCommonMultiple2([n * m] + numList[2:])
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
		return int(LowestCommonMultiple2([lcm] + numList[2:]))

def HighestCommonFactor(n, m):
	"""Will return the highest common factor of the two inputs (should be convertable into integers)"""
	# Code is borrowed from lcm and modified
	n = int(n)
	m = int(m)
	nFacList = FindFactors(n)
	nFacList.append(n)  # n is factor of n
	mFacList = FindFactors(m)
	mFacList.append(m)  # m is factor of m
	commonFactors = []
	factor = 1
	highestCommon = 1
	for x in range(len(nFacList)):  # Attempts to create list of common prime factors, the most amount of times they occur
		for y in range(len(mFacList)):
			factor = nFacList[x]
			if nFacList[x] == mFacList[y] and commonFactors.count(factor) == 0:  # Common factors
				commonFactors.append(factor)
				if factor > highestCommon:
					highestCommon = factor
	return highestCommon

def HCFEuclid(a, b):
	a = int(a)
	b = int(b)
	if a < b:
		temp = b
		b = a
		a = temp
	r = 1
	while r != 0:
		r = a % b
		temp = b
		b = a
		a = temp
	return a

def HCFEuclid2(n, m):
	n = int(n)
	m = int(m)
	if n < m:
		temp = m
		m = n
		n = temp
	r = 1
	while r != 0:
		r = n % m
		temp = m
		m = n
		n = temp
	return n

def EuclideanAlgorithm(b, a):
	"""Returns the greatest common divisor of a and b using the Euclidean Algorithm.
	This function is also known as gcd() or hcf().

	Arun I think you already programmed this above, so now we have to race our algorithms to the
	death..."""

	if a == 0 or b == 0:
		if a == 0 and b == 0:
			return 0
		else:
			return 1
	if b % a != 0:
		return EuclideanAlgorithm(a, b % a)
	else:
		return a

def BezoutCoefficients(a, b):
	"""Generates two Bezout coefficients, s and t, satisfying Bezout's identity as + bt = gcd(a, b).
	Pseudocode from https://www.dcode.fr/bezout-identity

	N.B. doesn't work."""

	r1 = a
	r2 = b
	u1 = 1
	u2 = 0
	v1 = 0
	v2 = 1

	while r2 != 0:
		q = int(r1 / r2)
		rs = r1
		us = u1
		vs = v1
		r = r2
		u = u2
		v = v2
		r2 = rs - q * r2
		u2 = us - q * u2
		v2 = vs - q * v2
	return r, u, v

def Gamma(a):
	"""Gamma function, the generalised factorial. The function Γ such that Γ(α + 1) = αΓ(α). Takes
	any real number greater than 0."""

	if a > 1:
		return (a - 1) * Gamma(a - 1)
	else:
		return a

def Factorial2(n):
	"""Mathematical factorial function. Works the same as the usual approach, but it uses the Gamma
	function. Mathematically pleasing. Gauss-approved. Takes an integer n >= 0.

	Note: Gamma(1/2)**2 should equal pi - I don't think it works for non-integers."""

	return Gamma(n + 1)


if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""

	for x in range(20):
		print(x)
		print(BaseConverter(x, 10, 16))
		print(hex(x))
		print()
