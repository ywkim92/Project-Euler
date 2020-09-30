# 1st way: this takes too long.
def issquare(num):
    root = math.sqrt(num)
    if int(root+0.5)**2==num:
        return True
    else:
        return False

limit = 10**9//6
result = []

# area of triangle S = sqrt(s * (s - a) * (s - b) * (s - c))
for i in range(2,limit):
    if issquare(((3*i+1)*(i+1))) == True:
        print(6*i+2)
		result.append(6*i+2)
		
    elif issquare(((3*i-1)*(i-1))) == True:
        print(6*i-2)
		result.append(6*i-2)

''' output
16
50
196
722
2704
10082
37636
140450
524176
1956242
7300804
27246962
101687056
379501250'''

print(sum(result))
# answer: 518408346
