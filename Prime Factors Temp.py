#-------------------------------------------------------------------------------
# Name:        Prime Factors

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

def FindPrimeFactors(n):
	"""Will return a list of the prime factors, repeated as many times as to produce n"""

	pFactors = []
	for x in range(2,n//2+1):
		if n%x == 0:
			if IsPrime3(x):
				pFactors.append(x)
				if IsPrime3(n//x):
					pFactors.append(n//x)
				else:
					reccursive = FindPrimeFactors(n//x)
					for i in range(len(reccursive)):
						pFactors.append(reccursive[i])
			else:
				reccursive = FindPrimeFactors(n//x)
				for i in range(len(reccursive)):
					pFactors.append(reccursive[i])
			return pFactors

print(FindPrimeFactors(int(input(""))))