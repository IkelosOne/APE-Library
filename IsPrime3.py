#-------------------------------------------------------------------------------
# Name:        IsPrime 3 - This Is Gonna Get Meaty

#A good number to test for primes is 9843498239573897

primeList = []

def IsPrime(n): #Version 3 - Time 16.04
    """Input n, returns True if n is prime and False if not."""
    if n > 2:
        if n % 2 == 0:
            return False
        x = 1
        while x*x <= n: # x*x<n is much more efficient than x<sqrt(n)
            if (n % x) == 0:
                return False
            x += 2
        return True
    else:
        if n ==2:
            return True
        return False

print(IsPrime(int(input(""))))