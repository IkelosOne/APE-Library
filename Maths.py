def GeneratePrimesUnderN(n):  # Can't get this to work
	"""Input n >= 6, Returns a list of primes, 2 <= p < n."""

	n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
	sieve = [True] * (n // 3)
	for i in range(1, int(n**0.5) // 3 + 1):
		if sieve[i]:
			k = 3 * i + 1 | 1
			sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
			sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
	return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

def IsPrime(n):
	"""Input n, returns True if n is prime and False if not."""

	if n > 1:
		for i in range(2, n ** 0.5):
			if (n % i) == 0:
				return False
		else:
			return True
