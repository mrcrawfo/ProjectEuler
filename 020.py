def factorial(n):
    r = 1
    for x in range(1, n + 1):
        r *= x
    return r

def sumDigits(n):
    s = str(n)
    r = 0
    for c in s:
        r += int(c)
    return r

print(str(sumDigits(factorial(100))))
