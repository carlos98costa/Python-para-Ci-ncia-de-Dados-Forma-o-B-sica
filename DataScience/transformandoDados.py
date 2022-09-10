import pandas as pd
import numpy as np

##00

df = pd.DataFrame(np.arange(36).reshape(6, 6))
#print(df)

##01 removendo dados

#print(df.drop([0, 2]))

#print((df.drop([1, 2], axis=1)))

##02 acrescentando dados

serie = pd.Series(np.arange(6))
serie.name = 'nova_variavel'
#print(serie)

novo_df = pd.DataFrame.join(df, serie)

#print(novo_df)

##03 ordenando dados

df_ordenado = novo_df.sort_values(by=['nova_variavel'], ascending=False)
print(df_ordenado)