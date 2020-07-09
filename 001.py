def isSumOf3(n):
    return ((n % 3) == 0)

def isSumOf5(n):
    return ((n % 5) == 0)

sum = 0
for i in range(1000):
    if (isSumOf3(i) or isSumOf5(i)):
        sum += i

print(sum)