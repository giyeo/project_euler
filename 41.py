from lib import *

def do():
    chars = "123456789"
    for i in range(1_000_000_000, 899_000_000, -1):
        str_i = str(i)
        l = len(str_i)
        for d in chars[0:l]:
            str_i = str_i.replace(d, "", 1)
        if not len(str_i):
            print(i)
            #if isPrimeFast(i):
            #    print(i)

def do2():
    for i in range(20_000_000, 0, -1):
        str_i = str(i)
        l = len(str_i)
        for j, d in enumerate(str_i):
            if d in str_i[j + 1:]:
                break
            if int(d) == 0 or int(d) > l:
                break
        else:
            if isPrimeFaster(i):
                print("FOUND!:", i) 
                return
            
def do2Old():
    for i in range(20_000_000, 0, -1):
        str_i = str(i)
        l = len(str_i)
        for j, d in enumerate(str_i):
            if d in str_i[j + 1:]:
                break
            if int(d) == 0 or int(d) > l:
                break
        else:
            if isPrimeFast(i):
                print("FOUND!:", i) 
                return

def do3():
    for i in range(20_000_000, 0, -1):
        str_i = str(i)
        l = len(str_i)
        seen_digits = set()

        valid = True
        for d in str_i:
            if d in seen_digits or int(d) == 0 or int(d) > l:
                valid = False
                break
            seen_digits.add(d)

        if valid and isPrimeFaster(i):
            print("FOUND!:", i)
            return
#res: 7652413


import time

start = time.time()
do2()
end = time.time()
print(end - start)

start = time.time()
do2Old()
end = time.time()
print(end - start)



#crazy statement
#The sum of digits in a pandigital number 1 1 to 𝑛 n is 𝑛 ( 𝑛 + 1 ) 2 2 n(n+1) ​ . If the sum of digits is divisible by 3, the number is not prime. This eliminates pandigital numbers for 𝑛 = 9 , 8 , 6 , 5 , 3 n=9,8,6,5,3, etc. Only 𝑛 = 7 , 4 , 1 n=7,4,1 are potentially prime.