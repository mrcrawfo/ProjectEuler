def sumDigits(n):
    a = list(str(n))
    sum = 0
    for x in a:
        sum += int(x)
    return sum

print(sumDigits(int(2**1000)))
