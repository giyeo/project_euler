#sum all primes below 2 000 000
from lib import isPrimeFast
soma = 2
for i in range(3, 2_000_000, 2):
    if isPrimeFast(i):
        soma += i
print(soma)

#pythonice!
print(sum(i for i in range(3, 2_000_000, 2) if isPrimeFast(i)) + 2)
#i will read it for you.
#sum all the values of i for each in range of 3 to 2 mil, jumping 2 at a time, but only if they are prime, then sum 2
