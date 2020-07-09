import math

def isEven(n):
    return ((n % 2) == 0)

def isPrime(n):
    if isEven(n) and n != 2:
        return False
    
    if n >= 3:
        for x in range(3, math.floor(n / 2), 2):
            if ((n % x) == 0):
                return False
    elif n == 2:
        return True
    else:
        return False
    
    return True

def findPrimeFactors(n):
    pf = []
    for x in range(2, math.floor(n / 2), 1):
        if ((n % x) == 0):
            if isPrime(x):
                pf.append(x)
                d = math.floor(n / x)
                if isPrime(d):
                    pf.append(d)
                else:
                    pf = pf + findPrimeFactors(d)
            else:
                pf = pf + findPrimeFactors(x)
                
        #breakout if pf values equal n
        sum = 1
        for f in pf:
            sum = sum * f
        if sum == n:
            return pf
    return pf

#print(findPrimeFactors(12)) # expecting [2, 2, 3]
#print(findPrimeFactors(147)) # expecting [3, 7, 7]
#print(findPrimeFactors(13195)) # expecting [5, 7, 13, 29]

print(findPrimeFactors(600851475143))