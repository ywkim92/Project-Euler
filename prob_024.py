import itertools
p24 = list( itertools.permutations(list(str(a) for a in range(10)), 10) )
p024 = list( ''.join(list(p24[i])) for i in range( len(p24) ) )
p024.sort()

print( int(p024[999999]) )
# output: 2783915460
