import matplotlib.pyplot as plt
import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
n = data1.groupby('Condition of the House')['ID'].count()
print(n)
values = (30,1701,14031,5679,172)
labels = ('Bad', 'Excellent', 'Fair', 'Good', 'Okay')
plt.pie(values, labels = labels)
plt.show()