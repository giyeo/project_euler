from lib import isPrimeFast

primeSet = set()
primeSet.add(2)
for i in range(3, 1_000_000, 2):
    if(isPrimeFast(i)):
        primeSet.add(i)
print(len(primeSet))

