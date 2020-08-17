def IsPrime(n):  # Version 3 - Time 16.04
	"""Input n, returns True if n is prime and False if not."""

	if n > 1:
		x = 2
		while x * x <= n:  # x*x<n is much more efficient than x<sqrt(n)
			if (n % x) == 0:
				return False
			x += 2
		return True
	else:
		return False


if __name__ == "__main__":
	print(IsPrime(3))
