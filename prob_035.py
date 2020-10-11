def primes(n):
    st = set(range(2, n+1))
    for i in range(2, n+1):
        if i in st:
            st -= set(range(2*i, n+1, i))
    return st

primeset = primes(1000000)
primeset -= {2,3,5,7}

answer = []
for i in primeset:
    if i in answer:
        continue
    num = str(i)
    count = 1
    cases = [i]
    
    while count < len(num):
        new = num[count:] + num[:count]
        if int(new) in primeset:
            count +=1
            cases.append(int(new))
        else:
            break
    
    if count == len(num):
        answer += cases

print( len(set(answer)) + len({2,3,5,7}) )
# output: 55
