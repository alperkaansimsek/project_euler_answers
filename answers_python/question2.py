preNum = 0
counter = 1
num = 1
sum = 0


while(counter <= 32):
    fib = preNum + num
    preNum = num
    num = fib
    if(fib % 2 == 0):
        sum = sum + fib
    counter = counter + 1


print(sum)
