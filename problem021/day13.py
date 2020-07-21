def divisorArray(num):
    divisor = []
    for i in xrange(1, num/2 + 1, 1):
        if num%i == 0:
            divisor.append(i)
    return divisor





amical = []
for n in xrange(1, 10000, 1):
    a = sum(divisorArray(n))
    b = sum(divisorArray(a))
    if n == b and n != a:
        amical.append(n)

print sum(amical)