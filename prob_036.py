def bi(n):
    if n==1:
        return '1'
    else:
        b=''
        while n>1:
            b=str(n%2)+b
            n=n//2
        return '1'+b

prob36=[]
for a in range(1, 1000000):
    if str(a) == str(a)[::-1] and bi(a) == bi(a)[::-1]:
        prob36.append(a)
        
print( sum(i for i in prob36) )
#output = 872187
