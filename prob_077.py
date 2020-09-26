def primes(n):
    st = set(range(2,n+1))
    for i in range(2, n+1):
        if i in st:
            st -= set(range(2*i, n+1, i))
    return st

# This function returns how many different ways writing ten as the sum of primes in.
def primesum(n):
    s = [1]+[0]*n
    cases = primes(n)
    
    for case in cases:
        for i in range(len(s) - case):
            s[i+case] += s[i]
    return s[-1]

i = 10
while 1:
    if primesum(i) >= 5000:
        print(i)
        break
    else:
        i += 1
# output: 71
