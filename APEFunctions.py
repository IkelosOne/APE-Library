def IsPrime(n):
	"""Input n, returns True if n is prime and False if not."""
	if n > 1:
		x = 2
		while x * x <= n:  # x * x < n is much more efficient than x < sqrt(n)
			if (n % x) == 0:
				return False
			x += 1
		return True
	else:
		return False

def IsPrime2(n):  # Formerly IsPrimeLightSpeed
	"""Assumes that n is a positive natural number.
	Source: https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not"""

	# We know 1 is not a prime number
	if n == 1:
		return False

	i = 2
	# This will loop from 2 to int(sqrt(x))
	while i * i <= n:
		# Check if i divides x without leaving a remainder
		if n % i == 0:
			# This means that n has a factor in between 2 and sqrt(n)
			# So it is not a prime number
			return False
		i += 1
	# If we did not find any factor in the above loop,
	# then n is a prime number
	return True

def IsPrime3(n):  # Version 3 - Time 16.04
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

def MakeBool(string):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	if string == "False":
		return False
	if string == "True":
		return True
	else:
		print("Impossible")

def InsertCommas(number):
	"""Inserts commas into the corresponding places in a number."""

	string = str(number)
	newString = string
	commasNeeded = len(str(number)[:-1]) // 3
	while commasNeeded > 0:
		newString = newString[:-(3 * commasNeeded)] + "," + newString[-(3 * commasNeeded):]
		commasNeeded -= 1
	return newString

def ReverseIt(inp):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	"""Takes string or int and return reversed version as string."""

	inp = str(inp)
	revNum = ""
	for x in range(len(inp)):
		digit = inp[len(inp) - x - 1]
		revNum += digit
	return revNum

def IsPalendromic(n):
	"""Returns True if n is palendromic and False if not."""

	n = str(n)
	for x in range(len(n)):
		if n[x] != n[len(n) - x - 1]:
			return False
	return True

def OccurencesInList(item, list1):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	"""Returns the amount of occurences of an item in a list."""

	count = 0
	for x in range(len(list1)):
		if list1[x] == item:
			count += 1
	return count


if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""

	None
