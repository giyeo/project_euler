#1 1 2 3 5 8 13...
a = 1
b = 1
soma = 0
while b < 4000000:
    temp = a
    a = b
    b = a + temp
    if b % 2 == 0:
        soma += b
print(soma)
