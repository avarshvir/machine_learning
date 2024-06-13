import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# Generate some sample data
np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))

# Fit SVR model
svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr.fit(X, y)

# Plot the results
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X, svr.predict(X), color='navy', lw=2, label='SVR')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
