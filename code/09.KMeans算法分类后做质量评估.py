# coding=utf-8
# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = [
    [9670250,  1392358258],
    [2980000,  1247923065],
    [9629091,  317408015],
    [8514877,  201032714],
    [377873,  127270000],
    [7692024,  23540517],
    [9984670,  34591000],
    [171244422,  143551289],
    [513115,  67041000],
    [181035,  14805358],
    [99600,  50400000],
    [120538,  24052231]
]

X = np.array(X)

a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a, b), axis=1)

# 类簇数量
n_clusters = 3

cls = KMeans(n_clusters).fit(X)

# 每个簇的中心点
cls.cluster_centers_

# X 中每个点所属的簇
cls.labels_

# 曼哈顿距离


def manhattan_distance(x, y):
    return np.sum(abs(x - y))


# a(v), X[0] 到其它点的距离的平均值
distance_sum = 0
for v in X[1:]:
    distance_sum += manhattan_distance(np.array(X[0]), np.array(v))
av = distance_sum / len(X[1:])

print(av)

# b(v), X[0]
distance_min = 100000
for i in range(n_clusters):
    group = cls.labels_ == i
    members = X[group, :]
    for v in members:
        if np.array_equal(v, X[0]):
            continue
        distance = manhattan_distance(np.array(v), cls.cluster_centers_)
        if distance_min > distance:
            distance_min = distance
bv = distance_sum / n_clusters
print(bv)

sv = float(bv - av) / max(av, bv)
print(sv)
