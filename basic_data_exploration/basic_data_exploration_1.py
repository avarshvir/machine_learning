import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
#print(data1.dtypes)
#print(data1.head(10))
#print(data1.describe())
#print(data1.describe(include = 'all'))
print(data1.info())