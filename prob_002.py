def fib(n):
    if n==0 or n==1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2,n+1):
            temp = a+b
            a = b
            b = temp
        return b
		
i = 1
total = 0
while fib(i)<4000000:
    f = fib(i)
    if f%2==0:
        total += f
    i+=1
	
print(total)
#output: 4613732
