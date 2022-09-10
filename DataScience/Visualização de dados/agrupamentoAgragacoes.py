import pandas as pd


##00
caminho = 'C:/Users/carlo/Documents/GitHub/Python-para-Ciencia-de-Dados/dados/mtcars.csv'

carros = pd.read_csv(caminho)
#print(carros.head())

carros.columns = ['nomes', 'mpg', 'cyl', 'disp', 'hpt', 'drat',
                  'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

#print(carros.head())

##01 agrupando dados por uma coluna
coluna_agrupamento = carros['cyl']
grupos_carros = carros.groupby(coluna_agrupamento)
print(grupos_carros.mean())