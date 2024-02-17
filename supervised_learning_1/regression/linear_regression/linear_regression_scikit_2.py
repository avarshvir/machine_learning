#implementation of linear_regression_1.py using scikit
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4]]   #input vector
y = [2,4,6,8]   #outputs

model = LinearRegression()


model.fit(X,y)

new_input = [[10]]
predicted_output = model.predict(new_input)
print("Predicted Output:",predicted_output)