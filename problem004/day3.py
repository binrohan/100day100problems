def isPalindrome(num):
    original = num
    reversedNum = 0
    while num != 0:
          reversedNum = reversedNum*10 + num%10
          num /= 10
    if original == reversedNum:
        return True
    return False


max = 0
for outer in range(1, 1000, 1):
    for inner in range(1, 1000, 1):
        if isPalindrome(outer*inner):
            if max < outer*inner:
                max = outer*inner
        
        
print max
