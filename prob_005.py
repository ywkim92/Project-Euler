def primeq(n):
    if n==1 or n==0:
        return False
    elif n==2 or n==3 or n==5 or n==7:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, n//2, 2):
            if n%i==0:
                return False
        return True

primes = []
for i in range(2,20):
    if primeq(i)==True:
        primes.append(i)
        
factors = dict()
ans = 1
for prime in primes:
    power = 0
    while prime**power<20:
        power+=1
    #factors[prime] = power-1
    ans *= prime**(power-1)
    
print(ans)
#output: 232792560
