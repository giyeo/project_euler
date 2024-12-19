from math import sqrt
from lib import isPrimeFast

n = 600851475143
i = int(sqrt(n))

print(i)
while i:
	if isPrimeFast(i):
		if n % i == 0:
			print(i)
			break
	i -= 1