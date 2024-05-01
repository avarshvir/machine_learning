import pandas as pd
data = pd.read_csv('E:\Python Project\Machine Learning\machine_learning\datasets\iris.csv')
print(data)
data.dropna(inplace=True)
print(data)

#manully spliting data
#input = x
#output = y
x = data.iloc[:,:4]    #as i need all row and 4 columns
print(x)

y = data.iloc[:,4]   #need all row of 5th column
print(y)

#training and testing
x_train = x.iloc[:100]
x_testing = x.iloc[100:]
print(x_train)
print(x_testing)

y_train = y[:100]
y_testing = y[100:]
print(y_train)
print(y_testing)