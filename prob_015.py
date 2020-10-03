# I defined factorial as 'fac' and combination i.e. binomial coefficient as 'com'.
def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)

def com(n, r):
    return int( fac(n)/(fac(n-r)*fac(r)) )

print( com(40, 20) * com(20, 20) )
# output: 137846528820
