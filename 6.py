#this method is a brute force approach, i know there is math formulas for both
#i just dont want to do it ;^)

def sumOfSquareUpToN(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i * i
    return soma

def pythonicSumOfSquareUpToN(n):
    return sum(i * i for i in range(1, n + 1))

def squareOfTheSumUpToN(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma * soma

def pythonicSquareOfTheSumUpToN(n):
    return sum(i for i in range(1, n + 1)) ** 2


n = 100
print(squareOfTheSumUpToN(n) - sumOfSquareUpToN(n))

print(pythonicSquareOfTheSumUpToN(n) - pythonicSumOfSquareUpToN(n))

