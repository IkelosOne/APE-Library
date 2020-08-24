#-------------------------------------------------------------------------------
# Name:        LowestCommonMultiple3

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

def LowestCommonMultiple2(numList):  # Good to test with 12345678911111111111,98765432199999999999
	"""Will use prime factors to calculate lcm more efficiently for large inputs
	Version 2 - Time: 59.431"""

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

a = [0,1,2]
b = [3,4]
c = a+b
print(LowestCommonMultiple2([8,3,5])[0])