import pandas as pd
data1 = pd.read_csv("social_ads.csv")
mean_age = data1["Age"].mean()
print(f"Mean age: {mean_age:.2f}")

mean_all_columns = data1.mean()
print(mean_all_columns)

#variance
variance_all_columns = data1.var()
print(variance_all_columns)
