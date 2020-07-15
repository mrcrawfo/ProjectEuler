import math

def sumProperDivisors(n):
    if n == 1:
        return 1
    t = 1
    s = math.ceil(math.sqrt(n))
    for x in range(2, s):
        if ((n % x) == 0):
            t += x
            t += int(n / x)
    if s**2 == n:
        t += s
    return t

def sumOfAbundantNumbers(n):
    for x in abundantSet:
        if x > n:
            break
        if (n - x) in abundantSet:
            return True
    return False

abundantNumbers = []

for x in range(1, 28124):
    p = sumProperDivisors(x)
    if p > x:
        abundantNumbers += [x]

abundantSet = frozenset(abundantNumbers)

sum = 0

for x in range(1, 28124):
    if not sumOfAbundantNumbers(x):
        sum += x

print(sum)
