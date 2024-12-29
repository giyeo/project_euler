#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from itertools import product

digitToPower = {}
for digit in range(10):
    digitToPower[digit] = digit ** 5

store = []

#6×59049  =  354294. 
for n in range(10, 354294):
    soma = 0
    for digit in str(n):
        soma += digitToPower[int(digit)]
    if soma == n:
        store.append(n)

print(store)
print(sum(store))





