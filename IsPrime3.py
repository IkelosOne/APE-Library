#-------------------------------------------------------------------------------
# Name:        IsPrime 3 - This Is Gonna Get Meaty

#A good number to test for primes is 9843498239573897

primeList = []

def IsPrime(n): #Version 3 - Time 15.81
    """Input n, returns True if n is prime and False if not."""
    if n > 2:
        if n % 2 == 0:
            return False
        x = 3
        while x*x <= n: # x*x<n is much more efficient than x<sqrt(n)
            if (n % x) == 0:
                return False
            x += 2 #Only cycles through odd numbers
        return True
    else:
        if n ==2:
            return True
        return False

if __name__=="__main__":
    print(IsPrime(int(input(""))))