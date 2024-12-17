#my idea here is incrementing by the product of all primes below 20
#so you can do that in 24 iteractions, pretty nice, very fast.
#if you do one by one, it takes 232.792.560 iterations

it = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
i = it
count = 0
while i:
    count += 1
    for n in range(1,21):
        if i % n != 0:
            break
    else:
        print(i)
        break
    i += it
print(count)
