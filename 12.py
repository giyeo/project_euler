# Ceil = n
# While i != ceil
#   If n % i == 0 && ceil == n
#     Ceil = n // i + 1
#  i++
# i starts 2
#  If  n == 1, return 1
#  While i < ceil

#500 divisors

def getFactors(n):
    factors = [1]

    if(n < 1):
        return []
    if(n == 1):
        return factors
    
    ceil = int(n**0.5)
    for i in range(2, ceil):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    factors.append(n)
    return factors

soma = 0
maxx = 0
for i in range(1,50000):
    soma += i
    factors = getFactors(soma)
    l = len(factors)
    maxx = max(maxx, l)
    if i % 100 == 0:
        print(soma)
    if l > 500:
        print(soma)
        print(maxx)
        break