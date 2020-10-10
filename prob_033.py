for nu in range(10, 99):
    for de in range(nu+1, 100):
        if len( set(str(nu)).intersection(str(de)) ) == 1:
            common = str(*set(str(nu)).intersection(str(de))) 
            n = list(str(nu))
            n.remove(common)
            d = list(str(de))
            d.remove(common)
            nu1 = int(*n)
            de1 = int(*d)
            if common != '0' and de1 != 0 and nu/de == nu1/de1:
                print(nu, '/', de, '=', nu1, '/', de1, end='\n')

''' output:
16 / 64 = 1 / 4
19 / 95 = 1 / 5
26 / 65 = 2 / 5
49 / 98 = 4 / 8 '''

# 1/4 * 1/5 * 2/5 * 4/8 = 1/100. The answer is 100.
