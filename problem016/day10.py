import math

x = 2**1000

sum = 0
while x != 0:
    n = x%10
    sum += n
    x /= 10

print sum