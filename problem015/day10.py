import math 

def TotalPathInGrid(r, c):
    return math.factorial(r+c)/(math.factorial(r)*math.factorial(c))

result = TotalPathInGrid(20, 20)


print result