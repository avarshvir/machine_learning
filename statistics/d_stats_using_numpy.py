import pandas as pd
import numpy as np
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
data2 = np.std(data1['Sale Price'])
print(data2)
#fixing n - 1
print(np.std(data1['Sale Price'],ddof=1))
#functions of numpy
print(dir(np))