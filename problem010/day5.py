import math

def isPrime(num):
    for x in xrange(2, int(round(math.sqrt(num))) + 1, 1):
        if num%x == 0:
          return False
    return num!=1

sum = 77
n = 20
while n<2000000:
    n += 1
    if n>20 and n%2 != 0 and n%3 !=0 and n%4 !=0 and n%5 !=0 and n%6 != 0 and n%7 != 0 and n%8 != 0 and n%9 != 0 and n%11 != 0 and n%13 != 0 and n%17 != 0 and n%19 != 0:
        if isPrime(n):
            sum += n
    print n
print sum