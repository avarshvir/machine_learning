import matplotlib.pyplot as plt
import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
plt.title("Graphs")
plt.plot(data1['Sale Price'])
plt.plot(data1['Sale Price'],marker = 'o', markerfacecolor = 'blue', markersize = 5, color = 'green', linewidth = 5, linestyle = 'dashed')
plt.xlabel("Record Number")
plt.ylabel("Sale Price")
plt.show()
