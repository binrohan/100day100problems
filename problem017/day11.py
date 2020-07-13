from num2words  import num2words

def numberLetterCount(num):
    sum = 0
    for l in num2words(num):
        if l.isalpha():
            sum += 1
    return sum

    
sum = 0
for i in xrange(1, 1001, 1):
    sum = sum + numberLetterCount(i)
print sum