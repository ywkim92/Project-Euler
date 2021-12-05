from square_root import sqrt

def prime_set(n):
    if n==2:
        return {2}
    else:
        odd = set(range(3,n+1,2))
        primes = {2}.union(odd)
        for i in range(3, (n+1), 2):
            if i in primes:
                primes  -= set(range(i*2, n+1, i))
        return primes

def factorization(num):
  num_sqrt = sqrt(num,)
  prime_list = prime_set(int(num_sqrt)+1)

  factors = []
  for p in prime_list:
    if num%p==0:
      while num%p==0:
        factors.append(p)
        num//=p
    if num==1: break
    
  if num!=1: return factors + [num]
  else: return factors
