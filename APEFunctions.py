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