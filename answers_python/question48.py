number = 1
sum = 0

for i in range(1000):
    toSum = pow(number, number)
    sum = sum + toSum
    number = number + 1

print(sum)

#I selected last digits manually but you can try to take those digits automatically by dividing the number. 
