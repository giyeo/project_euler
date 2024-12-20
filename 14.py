def factorChainSize(n):
    size = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
            size += 1
        else:
            n = n * 3 + 1
            size += 1
    return size + 1

maxx = 0
num = 0

for i in range(1, 1_000_000):
    size = factorChainSize(i)
    if size > maxx:
        num = i
        maxx = size

print(num, maxx)


    
