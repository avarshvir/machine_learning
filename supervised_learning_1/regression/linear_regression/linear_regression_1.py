import numpy as np
class LinearRegression:
    def __init__(self):
        self.coef = None  #coefficients
        self.intercept = None   #intercept

    def fit(self,X,y):
        X = np.array(X)
        y = np.array(y)

        X = np.c_[np.ones((X.shape[0],1)),X]

        self.coef = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        self.intercept = self.coef[0]
        self.coef = self.coef[1:]

    def predict(self,X):
        X = np.array(X)

        X = np.c_[np.ones((X.shape[0],1)),X]

        return X.dot(np.concatenate(([self.intercept],self.coef)))

X = [[1],[2],[3],[4]]
y = [2,4,6,8]

model = LinearRegression()
model.fit(X,y)

new_input = [[5]]
predicted_output = model.predict(new_input)
print("Predicted Output:", predicted_output)