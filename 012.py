import math

def findFactors(n):
    f = []
    for x in range(1, math.ceil(math.sqrt(n))):
        if ((n % x) == 0):
            if int(n / x) == x:
                f.append(x)
            else:
                f.append(x)
                f.append(int(n / x))
    return f

def countFactors(n):
    return 1 + len(findFactors(n))

cf = 0
nn = 0
tn = 0

while cf <= 500:
    nn += 1
    tn += nn
    cf = countFactors(tn)

print(str(nn) + ' :: ' + str(tn) + ' :: ' + str(cf))