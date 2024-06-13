import matplotlib.pyplot as plt
import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
n = data1.groupby('Condition of the House')['ID'].count()
print(n)
plt.boxplot(data1['Age of House (in Years)'])
plt.xlabel("Age of House (in Years)")
plt.ylabel("No. of Record")
plt.show()