#the function Leng returns the list of Pythagorean triples of which sum equals to the argument n.

def length(n):
    result = []
    for i in range(3,int(n/2)):
        for k in range(i+1,int(n/2)):
            if i*i+k*k==(n-i-k)**2:
                result.append((i,k,n-i-k))
    return result

import numpy as np
print(np.prod( length(1000)[0] ))
# output: 31875000
