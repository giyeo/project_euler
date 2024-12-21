from lib import isPrimeFast
truncable_primes = []

primeSet = set()

def getTruncableLeftToRight(n):
    truncables = []
    i = 0
    l = len(str(n))
    while i < l:
        truncables.append(n % (10 ** i))
        i += 1
    return truncables

def getTruncableRightToLeft(n):
    truncables = []
    while n != 0:
        n //= 10
        truncables.append(n)
    return truncables

def getTruncables(n):
    truncables = []
    truncables.extend(getTruncableLeftToRight(n))
    truncables.extend(getTruncableRightToLeft(n))
    return truncables[1:-1]

i = 11
while len(truncable_primes) < 11:

    if isPrimeFast(i):
        primeSet.add(i)
        truncables = getTruncables(i)
        for t in truncables:
            if t in primeSet:
                continue
            if not isPrimeFast(t):
                break
            primeSet.add(t)
        else:
            truncable_primes.append(i)
    i += 1

print(truncable_primes)
print(sum(truncable_primes))


