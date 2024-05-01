def division (n, number):
    while n <= 20:
        if number % n != 0:
            return False
        n += 1
    print(number)
    return True



startingPoint = 40
n = 1
loopHolder = True
while loopHolder == True:
    smallestNumber = division(n, startingPoint)
    if smallestNumber == True:
        print(smallestNumber)
        loopHolder = False
    else:
        startingPoint += 1
        continue


