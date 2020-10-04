p13 = []
with open('./text_data/p013.txt','r') as file:
    for line in file:
        p13.append(int(line.strip('\n')))

print( int(str(sum(p13))[:10]) )
# output: 5537376230
