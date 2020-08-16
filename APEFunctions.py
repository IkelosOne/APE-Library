#APE Functions
#Made as a collection of useful functions by Arun - Pablo - Elia
"""
To import:

import sys
sys.path.append("E\Example\APE-Library")
import APEFunctions
"""

###############################################################
#A good number to test for primes is 9843498239573897

def IsPrime(n): #This has been optimised to now be 98% the speed of IsPrimeLightspeed (a funciton found on the internet)
    """Input n, returns True if n is prime and False if not."""
    if n > 1:
        x = 2
        while x*x <= n: # x*x<n is much more efficient than x<sqrt(n)
            if (n % x) == 0:
                return False
            x += 1
        return True
    else:
        return False

#print(IsPrime(int(input(""))))
###############################################################
def makeBool(string):
    if string=="False":
        return False
    if string=="True":
        return True
    else:
        print("Impossible")
###############################################################
def commaNumber(number):
    #Takes number and adds commas every 3 digits. Returns string
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
###############################################################
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
###############################################################
def ReverseIt(inp): #Takes string or int and return reversed version as string
    inp = str(inp)
    revNum = ""
    for x in range(len(inp)):
        digit = inp[len(inp)-x-1]
        revNum += digit
    return revNum
###############################################################
def IsPalendromic(number):
    number = str(number)
    for x in range (len(number)):
        if number[x] != number[len(number)-x-1]:
            return False
    return True
###############################################################
def OccurencesInList(item,list1): #Returns the amount of occurences of an item in a list
    count = 0
    for x in range(len(list1)):
        if list1[x] == item:
            count += 1
    return count




