def primes(n):
    st = set(range(2, n+1))
    for i in range(2, n+1):
        if i in st:
            st -= set(range(2*i, n+1, i))
    return st

primeset = primes(1000)

#This function returns the period of decimal representation of 1/n. It refers to https://oeis.org/A051626.
def period(n):
    lpow = 1
    while True:
        for mpow in range(lpow-1, -1, -1):
            if (10**lpow - 10**mpow) % n == 0:
                return lpow - mpow
        lpow += 1

ans = (3, 1) #( prime, period(prime) )
for i in primeset:
    peri = period(i)
    if peri > ans[1]:
        ans = (i, peri)

print(ans[0])
# output: 983
