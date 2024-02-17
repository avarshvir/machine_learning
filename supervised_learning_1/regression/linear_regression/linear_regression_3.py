'''
the traditional statistical approach to linear regression, where the
coefficients (slope and intercept) are calculated directly from the provided data
using the least squares method. It does not involve training a machine learning
model or using any machine learning algorithms.
'''


import numpy as np
X = [[1],[2],[3],[4],[5]]
y = [1.2,1.8,2.6,3.2,3.8]

x_mean = 3
y_mean = 2.52
x_square_mean = 11
x_y_mean = 8.88
x_mean_square = 3*3

m = ((x_y_mean)-(x_mean)*(y_mean))/(x_square_mean-x_mean_square)

c = y_mean-(m*x_mean)

x = 12

e = 0

# y is dependent variable, x is independent variable, e is error
linear_regression_equation = y = c +m*x + e
print(linear_regression_equation)
