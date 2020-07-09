def isPallindromicNumber(n):
    s = str(n)
    a = list(s)
    a.reverse()
    r = ''.join(a)
    return s == r

mx = 0

for x in range(900, 1000):
    for y in range(900, 1000):
        z = x * y
        if isPallindromicNumber(z):
            if z > mx:
                mx = z

print(mx)