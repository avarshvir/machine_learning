import pandas as pd
data = pd.read_csv("E:\Python Project\Machine Learning\machine_learning\datasets\Social_Network_Ads.csv")
print(data)
X = data.iloc[:,[2,3]].values
y = data.iloc[:,4].values
print(X,y)
from sklearn.tree import DecisionTreeClassifier
dtclr = DecisionTreeClassifier(criterion= "gini", splitter= "random", random_state= 0)
