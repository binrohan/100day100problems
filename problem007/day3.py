def isPrime(num):
    for x in range(2, num, 1):
        if num%x == 0:
          return False
    return num!=1

count = 0
i = 0
while count!= 10001:
    i = i + 1
    if isPrime(i):
        count += 1
        prime = i

print prime