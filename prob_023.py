# the function 'pd' returns a sum of proper divisors of the argument n.
def pd(n):
    proper = set() # set of proper divisors
    for i in range(2, n//2 +1):
        if n%i == 0:
            if n//i in proper:
                proper.add(i)
                break
            else:
                proper.add(i)
                proper.add(n//i)
    return sum(proper) + 1

abundant=[]
for i in range(1, 28123):
    if pd(i) > i:
        abundant.append(i)

abun_sums = set()
for m in abundant:
    for n in abundant:
        abun_sums.add(m + n) 

non_abun_sums = set(range(1, 28123)) - abun_sums
print( sum(non_abun_sums) )
# output: 4179871
