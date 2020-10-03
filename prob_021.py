# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
def d(n):
    proper = set() # set of proper divisors
    for i in range(2, n//2 +1):
        if n%i==0:
            if n//i in proper:
                proper.add(i)
                break
            else:
                proper.add(i)
                proper.add(n//i)
    return sum(proper) + 1

sums = 0
for i in range(1, 10000):
    if i==d(d(i)) and i!=d(i):
        sums += i

print(sums)
# output 31626
