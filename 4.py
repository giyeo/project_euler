from itertools import product

a = 999
b = 999
palindromes = []
combinations = (list(product(range(a), range(b))))
for n in combinations:
	str_n = str(n[0] * n[1])
	for i in range(len(str_n) // 2):
		if(str_n[i] != str_n[-(i + 1)]):
			break
	else:
		palindromes.append(n[0] * n[1])

print(sorted(palindromes)[-1])
		