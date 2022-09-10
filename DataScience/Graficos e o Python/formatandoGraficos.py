import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

##00
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

cor = ['green']

#plt.bar(x, y, color=cor)
#plt.show()

##01 customizando estilos das linhas

x1 = range(0, 10)
y1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#plt.plot(x, y)
#plt.plot(x1, y1)
#plt.show()

##02
#plt.plot(x, y, ls='dotted', lw=5)
#plt.plot(x1, y1, ls='--', lw=10)
#plt.show()

##03 definindo marcadores em graficos

plt.plot(x, y, marker='1', mew=20)
plt.plot(x1, y1, marker='+', mew=15)
plt.show()
