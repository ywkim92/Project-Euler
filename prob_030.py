prob30=[]
for i in range(2,1000000):
    if i == sum(int(n)**5 for n in str(i)):
        prob30.append(i)

print( sum(prob30) )
# output: 443839
'''4150
4151
54748
92727
93084
194979'''
