#descriptive statistics for single variable
import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
print(data1['Sale Price'].mean())
print(data1['Sale Price'].max())
print(data1['Sale Price'].min())
print(data1['Sale Price'].std())
print(data1['Sale Price'].var())

print(data1['Sale Price'].quantile(.25))
print(data1['Sale Price'].quantile(.50))
print(data1['Sale Price'].quantile(.75))
#unique is usually used for string or categorical variable
print(data1['Condition of the House'].unique())