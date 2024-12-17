from math import sqrt
import time

def fib(i):
    a = 0
    b = 1
    while i:
        temp = a
        a = b
        b = a + temp
        i -= 1
    return b

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPrimeFast(n):
    if n == 1:
        return False
    if n == 2:
        return True

    i = 3
    sq = sqrt(n)
    while i <= sq:
        if n % i == 0:
            return False
        i += 2
    return True
