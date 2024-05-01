def collatz_sequence(n):
    collatzCounter = 1
        
    while n != 1:


        if(n % 2 == 0):
            n = n/2 
        elif(n % 2 != 0):
            n = (3 * n) + 1


        if n not in usedNumbers:
            usedNumbers.append(n)


        collatzCounter += 1
    #collatzChains.append(collatzCounter)
    return collatzCounter
        

number = 1
tempCollatz = 1
usedNumbers = []
collatzChains = [0]

CollatzNumbers = {
    
}

while number < 1000000:
    longestCollatz = collatz_sequence(number)
    if(number in usedNumbers):
        number += 1
        continue
    
    if(longestCollatz > tempCollatz):
        tempCollatz = longestCollatz
        bigNumber = number
        
    else:
        longestCollatz = longestCollatz
        number = number
    tempCollatz -= 1
    CollatzNumbers.update({number:tempCollatz})
    number += 1


#print(CollatzNumbers)
print("longest collatz number is: ", bigNumber, "\n collatz chain: ", tempCollatz)
