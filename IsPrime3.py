#-------------------------------------------------------------------------------
# Name:        IsPrime 3 - This Is Gonna Get Meaty

#A good number to test for primes is 9843498239573897

primeList = []

def IsPrime(n): #Version 3
    """Input n, returns True if n is prime and False if not."""
    if n > 1:
        x = 2
        while x*x <= n: # x*x<n is much more efficient than x<sqrt(n)
            if IsPrime(x):
                if (n % x) == 0:
                    return False
            x += 1
        return True
    else:
        return False

print(IsPrime(int(input(""))))