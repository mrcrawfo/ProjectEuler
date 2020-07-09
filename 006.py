def sumOfSquares(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x**2
    return sum

def squareOfSum(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    return sum**2

print(str(squareOfSum(100) - sumOfSquares(100)))