# defining a function returns a set of primes <= input number.
def primes(n):
    st = set(range(2,n+1))
    for i in range(2, n+1):
        if i in st:
            st -= set(range(2*i, n+1, i))
    return st

print( sum(primes(2000000)) )
# output: 142913828922
