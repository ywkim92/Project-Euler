def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

print( sum( int(a) for a in str(fac(100)) ) )
# output: 648
