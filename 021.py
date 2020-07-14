import math

def sumProperDivisors(n):
    f = 0
    for x in range(1, math.ceil(math.sqrt(n))):
        if ((n % x) == 0):
            if int(n / x) == x:
                f += x
            else:
                f += x
                if x > 1:
                    f += int(n / x)
    return f

sum = 0

for x in range(10000):
    y = sumProperDivisors(x)
    if y != x and x == sumProperDivisors(y):
        print(str(x) + ' :: ' + str(y))
        sum += x

print('')
print(str(sum))