#PEA Functions
def IsPrime(n):
    """Input n, returns True if n is prime and False if not."""

    if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               return False
       else:
           return True

def makeBool(string):
    if string=="False":
        return False
    if string=="True":
        return True
    else:
        print("Impossible")

def commaNumber(number):
    #Takes number and adds commas every 3 digits
    number=str(number)
    numList=[]
    seperates=DIV(len(number),3)
    for x in range(seperates):#Repeats for the amount of commas
        leftLim=-(seperates+1-x)*3
        rightLim=-((seperates-x)*3)
        numList.append(number[leftLim:rightLim])
    numList.append(number[-3:])
    result=""
    for n in range(len(numList)):#Turns list into string
        result=result+","+numList[n]
    while result[0]==",":#Gets rid of commas at start
        result=result[1:]
    return result

def IsPrime(n):
	"""Input n, returns True if n is prime and False if not."""

	if n > 1:
		for i in range(2, n):
			if (n % i) == 0:
				return False
		else:
			return True

def IsPrimeLightspeed(n): #https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


