import pandas as pd
import numpy as np

from    pandas import DataFrame

##00
dados = {
    'coluna 1' : [1, 1, 2, 2, 3, 3, 3],
    'coluna 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna 3' : ['A', 'A', 'B', 'B', 'C', 'C', 'C']
}
df = DataFrame(dados)
#print(df)

##01 removendo dados duplicados

#print(df.duplicated())
#print(df.drop_duplicates())

df.drop_duplicates(inplace=True)
##print(df)

##02

dados = {
    'coluna 1' : [1, 1, 2, 2, 3, 3, 3],
    'coluna 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna 3' : ['D', 'A', 'B', 'B', 'C', 'C', 'C']
}
df = DataFrame(dados)

print(df.drop_duplicates(['coluna 3']))