import math

def check_pathagorean(a, b, c):
    return a**2 + b**2 == c**2

for a in range(1, 332):
    for b in range(a+1, int(math.ceil((1000-a)/2.-1))):
        c = 1000 - a - b
        if (check_pathagorean(a, b, c)):
            print a* b*c
            break