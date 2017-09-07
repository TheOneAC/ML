import random


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
    for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
        for v_i, w_i in zip(v, w)]
def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

class KMeans:
    def __init__(self, k):
        self.k = k
        self.means = None
    def classify(self,input):
        return min(range(self.k),
                   key = lambda i: squared_distance(input, self.means[i]))
    def train(self, inputs):
        self.means = random.sample(inputs,self.k)
        assignments = None
        while True:
            new_assignments = map(self.classify,inputs)
            if assignments == new_assignments:
                return
            assignments = new_assignments
            for i in range(self.k):
                i_points = [p for p,a in zip(inputs, assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)


random.seed(0)
clusterer = KMeans(2)
clusterer.train(inputs)
print clusterer.means