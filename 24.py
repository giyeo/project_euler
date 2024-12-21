from itertools import permutations

data = [0,1,2,3,4,5,6,7,8,9]
#data = [0,1,2]

p = list(permutations(data))
for digit in p[1_000_000 - 1]:
    print(digit, end="")

