sum = 0
for i in range(101):
    sum += i**2
    
sumAll = 0
for j in range(101):
    sumAll += j

sumAll = sumAll**2

print(sumAll - sum)
