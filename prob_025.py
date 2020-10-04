def digit_fib(n):
    a=1
    b=1
    c=2
    index = 2
    while len(str(c))<n:
        c=a+b
        a=b
        b=c
        index+=1
    return index

print( digit_fib(1000) )
# output: 4782
