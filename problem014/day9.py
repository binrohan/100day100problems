n = 13
max = [0,0]
ipo = 0
count = int(0)


def colantz(n,count=1):
    while n > 1:
        count += 1
        if n%2 == 0:
            n=n/2
        else:
            n= (3*n) +1
    return count

for i in range(1000000):
    ipo = colantz(i)
    if ipo > max[0]:
        max[0] = ipo
        max[1] = i

print max