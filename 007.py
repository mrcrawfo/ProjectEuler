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

i = 2
t = 10001
n = 1

while i <= t:
    n += 2
    if isPrime(n):
        i += 1

print(str(i - 1) + ' :: ' + str(n))