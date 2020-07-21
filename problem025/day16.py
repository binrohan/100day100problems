n = 1
a,b = 0,1
while True:
    a,b = b, a+b
    if a >= (10**(1000-1)):
        print ("index is  : ", n)
        break
    n += 1



