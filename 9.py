squares = {}
squares[0] = 0
squares[1] = 1
squares[2] = 4
#Naive solution, more memory less calculations, funny
for i in range(2, 1000):
    squares[i] = i ** 2
    c = squares[i]
    for j in range(1, i):
        for k in range(j):
            if squares[k] + squares[j] == c: 
                if k + j + i == 1000:
                    print(k * j * i)
                    exit(0)
