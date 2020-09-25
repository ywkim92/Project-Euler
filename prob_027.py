# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of, starting with n = 0.

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

def primes(n):
	st = set(range(2, n+1))
	for i in range(2, n+1):
		if i in st:
			st -= set(range(2*i, n+1, i))
	return st

# The function returns the maximum of consecutive values, n with respect to a and b.
def p27(a,b):
    n = 0
    result = b
    while isprime(result)==True:
        n+=1
        result = n**2 + a*n + b
    return n

# The constant term b should be a prime less than 1000. Because the polynomial has to be a prime when n = 0.
max_num = 60
ans = tuple()
for a in range(-999,1000,2):
    for b in primes(1000):
        if p27(a,b) > max_num:
            max_num = p27(a,b)
            ans = (a,b)

print(ans[0] * ans[1])
#output: -59231
