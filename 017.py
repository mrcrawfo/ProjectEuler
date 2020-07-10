import math

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numberToWord(n):
    if n == 1000:
        return "onethousand"
    elif n >= 100:
        h = math.floor(n / 100)
        s = ones[h] + "hundred"
        r = n % 100
        if r > 0:
            s = s + "and" + numberToWord(r)
        return s
    elif n >= 20:
        t = math.floor(n / 10)
        s = tens[t]
        r = n % 10
        if r > 0:
            s = s + ones[r]
        return s
    elif n >= 10:
        r = n % 10
        return teens[r]
    else:
        return ones[n]

sum = 0

for x in range(1, 1001):
    w = numberToWord(x)
    print(w)
    sum += len(w)

print("")
print(str(sum))