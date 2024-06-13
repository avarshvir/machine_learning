import matplotlib.pyplot as plt
import pandas as pd
data1 = pd.read_csv('../datasets/1. Regression - Module - (Housing Prices).csv')
"""plt.scatter(x = data1['Flat Area (in Sqft)'], y =  data1['Sale Price'], color = 'red')
plt.xlabel("Area")
plt.ylabel("Selling Price")
plt.title("Selling Price vs Area")"""

"""plt.scatter(x = data1['No of Bathrooms'], y = data1['Sale Price'], color = 'red')
plt.xlabel("No of Bathroom")
plt.ylabel("Selling Price")
plt.title("Selling Price vs No of Bathrooms")"""
plt.scatter(x = data1['Age of House (in Years)'],y = data1['Sale Price'], color = 'red')
plt.xlabel('Age of House')
plt.ylabel('Sale Price')
plt.title('Age of House vs Sale Price')
plt.show()