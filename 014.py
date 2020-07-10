import math

def isEven(n):
    return ((n % 2) == 0)

def iterate(n):
    if isEven(n):
        return int(n / 2)
    else:
        return 3 * n + 1
    
def findChain(n):
    r = [n]
    while n > 1:
        n = iterate(n)
        r.append(n)
    return r

mx = []

for x in range(1, 1000000):
    c = findChain(x)
    if len(c) > len(mx):
        mx = c

print(mx)
print('')
print(len(mx))
