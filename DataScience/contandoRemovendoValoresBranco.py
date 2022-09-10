import numpy as np
import pandas as pd

from pandas import Series, DataFrame

##00
em_branco = np.nan
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape(6, 6))
df.loc[3:5, 0] = em_branco
df.loc[1:4, 5] = em_branco
#print(df)

##01 contando valores em branco
#print(df.isnull().sum())

##02 removendo valores em branco
df.dropna()

print(df.dropna(axis=1))