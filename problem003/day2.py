import math

def isPrime(num):
    for x in range(2, num, 1):
        if num%x == 0:
          return False
    return num!=1

maxPrime = 0
number = 600851475143
for n in range(1, int(math.ceil(math.sqrt(number)))+1, 1):
    if number%n == 0 and isPrime(n):
        if maxPrime <= n:
            maxPrime = n
print maxPrime         

        










