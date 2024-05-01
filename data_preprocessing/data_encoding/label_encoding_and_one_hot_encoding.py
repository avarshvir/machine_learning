from sklearn import preprocessing
import pandas as pd
le = preprocessing.LabelEncoder()
data = pd.DataFrame({'animals': ['cats', 'dogs', 'horse']})
print(data)
le.fit(data)
encoded_data = le.transform(data)
print(encoded_data)

#one hot encoding
ohe = preprocessing.OneHotEncoder()
ohe.fit(data)
encoded_ohe_data = ohe.transform(data)
print(encoded_ohe_data.toarray())