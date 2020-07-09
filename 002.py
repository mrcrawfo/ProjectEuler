def isEven(n):
    return ((n % 2) == 0)

def fibonacci(x, y, z):
    #print(str(x) + ' :: ' + str(y) + ' :: ' + str(z))
    if (z > 1):
        return fibonacci(y, y + x, z - 1)
    else:
        return y

def fibonacci_steps(s):
    return fibonacci(1, 1, s)

sum = 0
times_to_run_below_4000000 = 0

for f in range(100):
    result = fibonacci_steps(f)
    if(result < 4000000):
        times_to_run_below_4000000 = f
        if(isEven(result)):
            sum += result

print(sum)