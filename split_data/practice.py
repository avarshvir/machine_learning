import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('../datasets/Transformed_Housing_Data2.csv')
print(data)
Y = data.iloc[:,0]
print(Y)
X = data.iloc[:,1:31]
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.3)
print(X_train.shape)
print(X_test.shape)