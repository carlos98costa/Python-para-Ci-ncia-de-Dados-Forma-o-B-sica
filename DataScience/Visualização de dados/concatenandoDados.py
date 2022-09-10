import pandas as pd
import numpy as np

from    pandas import DataFrame

##00
df = pd.DataFrame(np.arange(36).reshape(6, 6))

#print(df)
df2 = pd.DataFrame(np.arange(15).reshape(5, 3))
#print(df2)

#print(pd.concat([df, df2]))

new = pd.concat([df, df2], axis=1)
print(new)
