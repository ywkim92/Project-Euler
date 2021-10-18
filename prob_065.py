import fractions

# cfe function: returning the list of the continued fraction representation of e, with n-digits
def cfe(n):
    cfe=[2]
    for i in range(1,round(n/3)+1):
        cfe.append(1)
        cfe.append(2*i)
        cfe.append(1)
    return list(cfe[l] for l in range(n))

for l in range(-1,-101,-1):
    if l==-1:
        r=cfe(100)[l]
    else:
        r=fractions.Fraction(1/r)+fractions.Fraction(cfe(100)[l])

print(sum(int(i) for i in list(str(r.numerator)))) #output: 272
