def count_digits(n):
    return(len(str(n)))

f = 1
c = 1
s = 1
complete = False

while complete == False:
    #print(str(s) + ' :: ' + str(c) + ' :: ' + str(count_digits(c)))
    old_f = f
    f = c + f
    c = old_f
    s += 1
    if(count_digits(f) >= 1000):
        complete = True

print('')
print(str(s + 1))
