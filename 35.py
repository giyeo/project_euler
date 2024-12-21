#circular primes bellow one million

from lib import isPrimeFast

def all_rotations_of_given_number(n):
    l = len(str(n))
    rotations = [n]
    for _ in range(l - 1):
        n = (n % 10) * 10 ** (l - 1) + (n // 10)
        rotations.append(n)
    return rotations

primeSet = set()
circularPrimeSet = set()

for i in range(10_000_000):
    rotations = all_rotations_of_given_number(i)
    for num in rotations:
        if num in primeSet:
            continue
        if not isPrimeFast(num):
            break
        primeSet.add(i)
    else:
        circularPrimeSet.add(i)

print(len(circularPrimeSet))
print(sorted(circularPrimeSet))