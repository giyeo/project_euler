from lib import isPrimeFast
from itertools import count, islice

#this one is very neat
def pythonicNthPrime(n):
    primes = (i for i in count(2) if isPrimeFast(i))
    return next(islice(primes, n - 1, n))

counter = 0
i = 1
while counter < 10001:
    i += 1
    if isPrimeFast(i):
        counter += 1
print(i)

print(pythonicNthPrime(10001))

    