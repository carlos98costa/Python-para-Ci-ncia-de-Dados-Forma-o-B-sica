import numpy as np
import pandas as pd

from pandas import Series, DataFrame

##00
dados = np.arange(8)
dados.reshape(4, 2)
#print(dados.reshape(4, 2))

indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4',
          'linha 5', 'linha 6', 'linha 7', 'linha 8']

##01
serie = Series(dados, index=indice)
#print(serie)
#print(serie ['linha 7'])

##02
np.random.seed(25)
indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5', 'coluna 6']
df = DataFrame(np.random.rand(36).reshape((6, 6)),
               index=indice,
               columns=colunas)
#print(df)
##print(df.loc[['linha 2', 'linha 4'], ['coluna 3', 'coluna 5']])

##03
print(serie['linha 3': 'linha 7'])