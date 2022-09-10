import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import rcParams

import seaborn as sns

##00
rcParams['figure.figsize'] = 5, 4
sns.set_style('whitegrid')

##01 criando grafico de linha a partir de uma lista
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

#plt.plot(x, y)
#plt.show()

##02 desenhando um grafico de linha usando um objeto pandas

caminho = 'C:/Users/carlo/Documents/GitHub/Python-para-Ciencia-de-Dados/dados/mtcars.csv'

carros = pd.read_csv(caminho)

carros.columns = ['nomes', 'mpg', 'cyl', 'disp', 'hpt', 'drat',
                  'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = carros[['cyl', 'mpg', 'wt']]
df.plot
plt.plot(df)
plt.show()