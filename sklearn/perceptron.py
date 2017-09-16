import numpy as np

class perceptron():
    def __init__(self,eta = 0.01,n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter
    def fit(self,X, Y):
        self.w = np.zeros(1 + X.shape[0])
        self.errors = []
        for _ in range(self.n_iter):
            errors = 0
            for xi,target in zip(X, y):
                update = self.eta * (y - self.predict(xi))
                self[1:] += update *xi
                self[0] += update
            errors += int(update != 0.0)
        self.errors.append(errors)
        return self
    def net_input(self,X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self,x):
        return np.where(self.net_input(X) >= 0.0,1,-1)


import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                     'machine-learning-databases/iris/iris.data', header = None)


import matplotlib.pyplot as plt

y = df.iloc[0:400,4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:400, [0,2]].values

plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()

ppn = perceptron(eta = 0.1, n_iter= 10 )
ppn.fit(X, y)
plt.plot(range(1 + len(ppn.errors)), ppn.errors, marker = 'o')