# This function finds all divisors of the number and returns to sum of them. 
def findDivisors(number):
    counter = number
    sumofDivisors = 0
    for i in range(1, counter):
        if(number % i == 0):
            sumofDivisors = i + sumofDivisors
    return sumofDivisors

  
# I know naming variables like that is not good for readability but I couldn't find better names.
# I started from 220 because I checked what is the lowest amicable pair and found that it was (220, 284).
a = 220
sum = 0

for a in range(a, 10000):
    b = findDivisors(a)
    c = findDivisors(b)
    if(c == a and b != c):
        sum = sum + a
        continue
    else:
        continue
print(sum)
