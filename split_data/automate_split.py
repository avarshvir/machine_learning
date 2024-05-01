#using sklearn
from sklearn.model_selection import train_test_split
import pandas as pd
data = pd.read_csv('E:\Python Project\Machine Learning\machine_learning\datasets\iris.csv')
#print(data)
data.dropna(inplace=True)
#print(data)

#input = x
#output = y
x = data.iloc[:,:4]    #as i need all row and 4 columns
#print(x)

y = data.iloc[:,4]   #need all row of 5th column
#print(y)
x_train, x_testing, y_train, y_testing = train_test_split(x,y,test_size=30,random_state=1)
print(x_train)
print(x_testing)
print(y_train)
print(y_testing)