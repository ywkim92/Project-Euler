count = 0
for i in range(2,10000001):
    sd = sum(int(j)**2 for j in str(i))   #sd: square digits sum
    while sd!=89 and sd!=1:
        sd = sum(int(k)**2 for k in str(sd))
    if sd == 89:
        count += 1

print(count)
# output: 8581146
