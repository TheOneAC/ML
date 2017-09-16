import pandas as pd
import numpy as np


df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                     'machine-learning-databases/iris/iris.data', header = None)


import matplotlib.pyplot as plt

y = df.iloc[0:400,4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:400, [0,2]].values



class AdaLineGD(object):
    def __init__(self,eta = 0.01, n_iter = 100):
        self.eta = eta
        self.n_iter = n_iter

    def net_input(self,X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.cost = []
        for _ in range(self.n_iter):
            output = self.net_input(X)
            error = y - output
            self.w[1:] += self.eta * X.T.dot(error)
            self.w[0] += self.eta * error.sum()
            cost = (error ** 2).sum()/ 2.0
            self.cost.append(cost)
        return self

    def activation(self,X):
        return self.net_input(X)

    def predict(self,xi):
        return np.where(self.activation(xi) >= 0.0,1,-1)


fig, ax = plt.subplots(nrows =1, ncols = 2, figsize=(8,3))

ada1 = AdaLineGD( eta= 0.0002).fit(X, y)
ax[0].plot(range(1, 1 + len(ada1.cost)), np.log10(ada1.cost), marker = 'o')
ax[0].set_xlabel("Epoch")
ax[0].set_ylabel("log(Sum-squared-error)")
ax[0].set_title('Adaline - Learning rate 0.0002')

ada1 = AdaLineGD(eta= 0.0001, ).fit(X, y)
ax[1].plot(range(1, 1 + len(ada1.cost)), np.log10(ada1.cost), marker = 'o')
ax[1].set_xlabel("Epoch")
ax[1].set_ylabel("log(Sum-squared-error)")
ax[1].set_title('Adaline - Learning rate 0.0001')

plt.show()