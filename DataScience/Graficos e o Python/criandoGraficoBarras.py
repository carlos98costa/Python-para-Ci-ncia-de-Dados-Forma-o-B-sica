import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import rcParams

##00
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

#plt.bar(x, y)
#plt.show()

##01
caminho = 'C:/Users/carlo/Documents/GitHub/Python-para-Ciencia-de-Dados/dados/mtcars.csv'

carros = pd.read_csv(caminho)

carros.columns = ['nomes', 'mpg', 'cyl', 'disp', 'hpt', 'drat',
                  'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = carros['mpg']
mpg.plot(kind='barh')
#plt.show()

##02

plt.savefig('grafico_de_barras_horizontais.png')