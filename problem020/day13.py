import math

def sumOfDigit(x):
    sum = 0
    while x != 0:
        n = x%10
        sum += n
        x /= 10
    return sum

x = math.factorial(100)
print sumOfDigit(x)
