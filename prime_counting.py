def prime_counting(n):
    if n==2:
        return 1
    else:
        odd = set(range(3,n+1,2))
        primes = {2}.union(odd)
        for i in range(3, (n+1)//3+1, 2):
            if i in primes:
                primes  -= set(range(i*2, n+1, i))
        return len(primes)
