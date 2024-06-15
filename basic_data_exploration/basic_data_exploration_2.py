import pandas as pd
import numpy as np
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
print(data1['Sale Price'])
print(data1['Sale Price'].tail(10))
print("Descriptive Statistics")
print(data1['Sale Price'].describe())
import matplotlib.pyplot as plt
#plt.scatter(x = data1['ID'], y = data1['Sale Price'])
#plt.show()
import seaborn as sns
#sns.boxplot(x = data1['Sale Price'])
#plt.show()

q1 = data1['Sale Price'].quantile(0.25)
q3 = data1['Sale Price'].quantile(0.75)
iqr = q3 - q1
print(iqr)

upper_limit = q3 + 1.5 * iqr
lower_limit = q3 - 1.5 * iqr
print(upper_limit, lower_limit)

def limit_imputer(value):
    if value > upper_limit:
        return upper_limit
    elif value < lower_limit:
        return lower_limit
    else:
        return value

data1['Sale Price'] = data1['Sale Price'].apply(limit_imputer)
print(data1['Sale Price'].describe())