inital = 0
current = 1
n = 0
sum = 0

while n <= 4000000:  
    if n%2 == 0:
          sum += n
    inital = current
    current = n
    n = inital + current


print sum


