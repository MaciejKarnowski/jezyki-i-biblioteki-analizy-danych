import numpy as np
import random
from math import sqrt
from collections import Counter

def euclidean_distance(x, y):
    return sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))


def manhattan_distance(x, y):
    return sum(abs(xi - yi) for xi, yi in zip(x, y))


def max_distance(x, y):
    return max(abs(xi - yi) for xi, yi in zip(x, y))


def dot_product(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def magnitude(v):
    return sqrt(dot_product(v, v))


def cosine_distance(v, w):
    return dot_product(v, w) / (magnitude(v) * magnitude(w))


class knn:
    X = []
    y = []

    def __init__(self, num_points, num_features, num_classes):
        self.num_features=num_features
        self.num_classes=num_classes
        self.generate_test_data(num_points, num_features, num_classes)

    def generate_test_data(self, num_points=None, num_features=None, num_classes=None):
        if self.X is None and self.y is None:
            for i in range(num_points):
                features = [random.randint(0, 100) for _ in range(num_features)]
                label = random.randint(0, num_classes - 1)
                self.X.append(features)
                self.y.append(label)
        else:
            for i in range(num_points):
                features = [random.randint(0, 100) for _ in range(self.num_features)]
                label = random.randint(0, self.num_classes - 1)
                self.X.append(features)
                self.y.append(label)
        return self.X, self.y

    def predict(self, test_point, k, distance):
        """Przewiduje etykietę dla podanego punktu przy użyciu algorytmu KNN.

           Arguments:
               X: lista list cech dla każdego punktu treningowego
               y: lista etykiet dla każdego punktu treningowego
               test_point: lista cech dla punktu, dla którego chcemy przewidzieć etykietę
               k: liczba najbliższych sąsiadów do uwzględnienia
               distance: funkcja obliczająca odległość między punktami

           Returns:
               int -- przewidywana etykieta dla test_point
           """
        distances = [(distance(test_point, self.X[i]), self.y[i]) for i in range(len(self.X))]
        sorted_distances = sorted(distances, key=lambda x: x[0])
        k_nearest_neighbors = [x[1] for x in sorted_distances[:k]]
        label_counts = Counter(k_nearest_neighbors)
        return label_counts.most_common()[0][0]


test = knn(100, 2, 5)
# print(test.X)
# print(test.y)
# print(len(test.X))
# print(len(test.y))
test.generate_test_data(100) #nalezy wpisać ile przypadków chce się dodać
# print(test.X)
# print(len(test.X))
# print(test.y)
# print(len(test.y))

print(test.predict([7, 2], 3, euclidean_distance)) #4 opcje:
                                                   # euclidean_distance
                                                   # manhattan_distance
                                                   # max_distance
                                                   # cosine_distance
