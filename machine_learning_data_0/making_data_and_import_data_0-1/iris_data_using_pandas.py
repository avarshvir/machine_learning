import pandas as pd
data = pd.read_csv('E:\Python Project\Machine Learning\machine_learning\datasets\iris.csv')
data.columns = ['sepal_length','sepal_width','petal_length','petal_width','labels']
print(data)

#for checking missing value -> isna(), isnull()
print("checking missing values")
print(data.isna())

print("checking missing values using isnull()")
print(data.isnull())

print("checking missing value for particular row")
print(data.isna().sum())

#for drop or delete record, we use -> dropna()
print("---------------dropping missing value------------------")
print(data.dropna())

#print(data)  -> it show again entire data set rows and columns
#for permanent drop we use, -> dropna(implace = True)
#data.dropna()

#thresh is used for removing column according to null value
print("-------------------thresh---------------------------")
print(data.dropna(thresh=5))

print("---------------how-----------------")
#if how = 'all' then record with all null value will drop
print(data.dropna(how = 'all'))