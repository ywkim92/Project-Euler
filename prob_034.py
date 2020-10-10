def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)

for i in range(3, 1000000):
    if i == sum(fac(int(n)) for n in str(i)):
        print(i)

# output: 145, 40585
# The answer is 145 + 40585 = 40730.
