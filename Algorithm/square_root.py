# by Babylonian method
def sqrt(n, loop=30):
    if loop==1: return (1+n)/2
    else:
        sq = sqrt(n, loop=loop-1)
        return (sq**2+n)/(2*sq)
