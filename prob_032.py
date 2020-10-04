x=list(str(i) for i in range(1,10))
A=list(i for i in range(2,9877) if '0' not in str(i))

prob32=set()
for h in list(r for r in A if r<100):
    for i in list(z for z in A if z>h):
        c=h*i
        if sorted(str(h)+str(i)+str(c))==x:
            prob32.add(c)

print(sum(i for i in prob32)) 
# output: 45228
