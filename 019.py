days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getDay(d):
    return days[d % len(days)]

year = 1900
c = 0
m = 0
while year < 2001:
    month = 1
    while month <= 12:
        date = 1
        daysInMonth = 0
        
        if year > 1900 and getDay(c) == "Sunday":
            m += 1
        
        if month in [4, 6, 9, 11]:
            daysInMonth = 30
        elif month == 2:
            if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
                daysInMonth = 29
            else:
                daysInMonth = 28
        else:
            daysInMonth = 31
            
        while date <= daysInMonth:
            #print(str(c) + ' :: ' + str(year) + '-' + str(month) + '-' + str(date) + ' :: ' + getDay(c))
            date += 1
            c += 1
        
        month += 1
    year += 1

print(str(c))
print(str(m))