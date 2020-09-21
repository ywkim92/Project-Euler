def nth_prime(n):
    primes = [2, 3, 5, 7]
    num = 9
    count = 4
    while count < n:
        for i in primes:
            if i>num//2:
                primes.append(num)
                count += 1
                num += 2
                break
                
            elif num % i == 0:
                num += 2
                break
            else:
                pass
    
    return primes[n-1]

print(nth_prime(10001))
# output: 104743
