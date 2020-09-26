p079_keys=[]
with open('p079.txt') as file:
    for line in file:
        line=line.replace('\n','')
        p079_keys.append(line)

p079_digits=set()
for i in p079_keys:
    s=set(i)
    p079_digits=p079_digits.union(s)
print(p079_digits) #output: {'0', '1', '2', '3', '6', '7', '8', '9'}

p079_0=set()
for i in p079_keys:
    p079_0.add(i[0])
print(p079_0) #output: {'1', '2', '3', '6', '7', '8'}

#by the same way, set of the 2nd and last digit are {'1', '2', '3', '6', '8', '9'}, {'0', '1', '2', '6', '8', '9'}, respectively.
#'7' is in the 1st digit only and '0' is in the last digit only. Therefore I assumed that the first and last digit of the shortest passcode are 7 and 0 respectively.

import itertools
p=list(itertools.permutations(p079_digits.difference({'0','7'}), 6))
p.sort()
passcodes=list(''.join(list(i)) for i in p)
passcodes=list('7'+i+'0' for i in passcodes)

for i in passcodes:
    count=0
    for key in p079_keys:
        passcode = i
        for j in range(3):           #because len(key)==3
            if key[j] not in passcode:
                break
            else:
                passcode = passcode.split(key[j])[1]
                count+=1
    if count==3*len(p079_keys):
        print(i)
#output: 73162890
