import pandas as pd
import numpy as np

from pandas import Series, DataFrame

##00
np.random.seed(25)
indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5', 'coluna 6']
df = DataFrame(np.random.rand(36).reshape((6, 6)),
               index=indice,
               columns=colunas)

#print(df)
#print(df < .2)

indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4',
          'linha 5', 'linha 6', 'linha 7', 'linha 8']
series_obj = Series(np.arange(8), index=indice)
filtro = series_obj > 6
#print(series_obj[filtro])

##01
series_obj['linha 1', 'linha 5', 'linha 8'] = 8
##print(series_obj)