import numpy as np

p11=[]
with open('./text_data/p011.txt', 'r') as file:
    for line in file:
        line=line.rstrip('\n').split(' ')
        line=list(int(a) for a in line)
        p11.append(line)

parallel=[]
for i in range(20):
    for j in range(17):
        parallel.append(np.prod(p11[i][j:j+4]))

perpendicular=[]
for i in range(20):
    for j in range(17):
        List = [p11[j][i],p11[j+1][i],p11[j+2][i],p11[j+3][i]]
        perpendicular.append(np.prod(List))

diagonal=[]
for x in range(20):
    for y in range(20):
        P=np.prod( list(p11[x+i][y+i] for i in range(4) if x+i<20 and y+i<20) )
        diagonal.append(P)

antidiagonal=[]
for x in range(20):
    for y in range(20):
        P=np.prod( list(p11[x+i][y-i] for i in range(4) if x+i<20 and y+i<20) )
        antidiagonal.append(P)

total = parallel+perpendicular+diagonal+antidiagonal
print( max(total) )
# output: 70600674
