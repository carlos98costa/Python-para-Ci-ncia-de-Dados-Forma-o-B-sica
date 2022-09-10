import  numpy as np
import pandas as pd

from pandas import Series, DataFrame

##00
em_branco = np.nan

serie = Series(['linha 1', 'linha 2', em_branco, 'linha 4', 'linha 5', em_branco, 'linha 7', 'linha 8'])

#print(serie)

##01
#print(serie.isnull())

np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape(6, 6))

#print(df)

##02
df.loc[3:5, 0] = em_branco

df.loc[1:4, 5] = em_branco

#print(df)

##03
df_preenchido = df.fillna(0)
#print(df_preenchido)

##04
dicio = {0: 0.1, 5: 1.25}
df_preenchido = df.fillna(dicio)
print(df_preenchido)
