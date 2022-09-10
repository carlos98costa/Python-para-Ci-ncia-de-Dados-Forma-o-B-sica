import pandas as pd

import matplotlib.pyplot as plt

##00
caminho = 'C:/Users/carlo/Documents/GitHub/Python-para-Ciencia-de-Dados/dados/mtcars.csv'

carros = pd.read_csv(caminho)

carros.columns = ['nomes', 'mpg', 'cyl', 'disp', 'hpt', 'drat',
                  'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = carros['mpg']

##01 colocando titulos nos eixos

x = range(1, 10)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1]
#plt.bar(x, y)
#plt.xlabel("Range X")
#plt.ylabel("Range Y")
#plt.show()

##02 colocando legenda no grafico
import matplotlib.patches as mpatches
""""""
"""
plt.plot(mpg)
plt.xlabel('Nome dos carros')
plt.ylabel('milhas/galão')
plt.title('Consumo de gasolina')
plt.xticks(mpg.index, carros.nomes, rotation=45)

legenda = mpatches.Patch(label='mpg')
plt.legend(handles=[legenda])
plt.show()
"""""

##03 fazendo anotacoes no grafico
plt.plot(mpg)
plt.xlabel('Nome dos carros')
plt.ylabel('milhas/galão')
plt.title('Consumo de gasolina')
plt.xticks(mpg.index, carros.nomes, rotation=45)

legenda = mpatches.Patch(label='mpg')
plt.legend(handles=[legenda])

"""plt.annotate('Toyota Corolla', xy=(19, 33.9), xyText=(21, 33), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()"""
