import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import seed




class AdaLineGD(object):
    def __init__(self,eta = 0.01, n_iter = 30,shuffle = True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.shuffle = shuffle
        self.w_inited = False
        if random_state:
            seed(random_state)

    def net_input(self,X):
        return np.dot(X, self._w[1:]) + self._w[0]

    def _shuffle(self, X, y):
        r = np.random.permutation(len(y))
        return X[r],y[r]
    def _init_weight(self, m):
        self._w = np.zeros(m + 1)
        self.w_inited = True
    def _update_weight(self, xi, target):
        output = self.net_input(xi)
        error = target - output
        self._w[1:] += self.eta * xi.dot(error)
        self._w[0] += self.eta * error
        cost =  0.5 * error ** 2
        return cost
    def fit(self, X, y):
        self._init_weight(X.shape[1])
        self.cost = []
        for _ in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weight(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost.append(avg_cost)
        return self

    def partial_fit(self, X, y):
        if not self.w_inited:
            self._init_weight(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weight(xi, target)
        else:
            self._update_weight(X, y)
        return self

    def activation(self,X):
        return self.net_input(X)

    def predict(self,xi):
        return np.where(self.activation(xi) >= 0.0,1,-1)


df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                     'machine-learning-databases/iris/iris.data', header = None)

y = df.iloc[0:400,4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:400, [0,2]].values

X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean())/ X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean())/ X[:,1].std()


fig, ax = plt.subplots(nrows =1, ncols = 1, figsize=(8,3))

ada1 = AdaLineGD(eta= 0.001).fit(X_std, y)
ax.plot(range(1, 1 + len(ada1.cost)), np.log10(ada1.cost), marker = 'o')
ax.set_xlabel("Epoch")
ax.set_ylabel("log(Sum-squared-error)")
ax.set_title('Adaline - Learning rate 0.001')


plt.show()