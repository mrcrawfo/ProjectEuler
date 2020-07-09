def isDivisibleBy(n, d):
    return ((n % d) == 0)

# product of all prime numbers from 1 to 20
inc = 9699690

spn = 0
esc = False

while esc == False:
    spn += inc
    div = True
    for n in range(1, 21):
        if not isDivisibleBy(spn, n):
            div = False
    esc = div

print(spn)