squares = []

for a in range(0, 1000):
    for b in range(a + 1, 1000):
        for c in range(b + 1, 1000):
            if ((a < b < c) and ((a**2) + (b**2) == (c**2)) and ((a + b + c) == 1000)):
                print('a :: ' + str(a))
                print('b :: ' + str(b))
                print('c :: ' + str(c))
