import math

def isBasicPrime(n):
    return ((n % 2) == 0) or ((n % 3) == 0) or ((n % 5) == 0)

def isPrime(n):
    if isBasicPrime(n) and n != 2 and n != 3 and n != 5:
        return False
    
    if n >= 3:
        for x in range(3, math.floor(math.sqrt(n)), 2):
            if ((n % x) == 0):
                return False
    elif n == 2:
        return True
    else:
        return False
    
    return True

sum = 0

for x in range(2000000):
    if isPrime(x):
        sum += x

print(sum)
