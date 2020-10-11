def primes(n):
    st = set(range(2, n+1))
    for i in range(2, n+1):
        if i in st:
            st -= set(range(2*i, n+1, i))
    return st

primeset = primes(1000000)

for i in primeset:
    if all( int(str(i)[k:]) in primeset for k in range(1, len(str(i))) )==True \
    and all( int(str(i)[:-l]) in primeset for l in range(1, len(str(i))) )==True :
        print(i)

''' output:
2
3
5
7
23
37
53
73
313
317
373
797
3137
3797
739397'''

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# sum of these eleven primes: 748317
