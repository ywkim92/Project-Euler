dic ={}
for num in range(1, 10**6+1):
    i = num
    count = 1
    while i>1:
        if i in dic:
            count += dic[i]-1
            break
        elif i%2==0:
            i//=2
            count +=1
        else:
            i = 3*i +1
            count+=1
    dic[num] = count

idx = 1
for i in range(1, 1000001):
    if dic[i]>dic[idx]:
        idx = i

print(idx)
# output: 837799
