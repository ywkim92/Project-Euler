from itertools import combinations
prob004 = []
cases = list(combinations(range(100,1000), 2))

for i in cases:
    if str(i[0]*i[1]) == str(i[0]*i[1])[::-1]:
        prob004.append(i[0]*i[1])

prob004.sort()
print(prob004[-1])
#output: 906609
