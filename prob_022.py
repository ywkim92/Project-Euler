import string
import pandas as pd

alphabet = list(string.ascii_uppercase)
dic = dict( zip(alphabet, range(1,27)) )

names = list(pd.read_csv('./text_data/p022_names.txt'))
names.sort()

product=[]
for i in names:
    product.append( (names.index(i)+1)*sum(dic[a] for a in list(i)) )

print( sum(a for a in product) )
# output: 871198282
