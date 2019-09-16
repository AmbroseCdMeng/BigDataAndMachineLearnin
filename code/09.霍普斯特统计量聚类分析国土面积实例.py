# coding=utf-8
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

# 数组转换
X = np.array(X)

# 归一化
a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a, b), axis=1)

pn = X[np.random.choice(X.shape[0], 3, replace=False), :]

# p 中随机选择 3 个

xn = []
for i in pn:
    distance_min = 1000000
    for j in X:
        if np.array_equal(j, i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance
    xn.append(distance_min)

qn = X[np.random.choice(X.shape[0], 3, replace=False), :]


# q 中随机选择 3 个

yn = []
for i in qn:
    distance_min = 1000000
    for j in X:
        if np.array_equal(j, i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance
    yn.append(distance_min)


H = float(np.sum(yn)) / (np.sum(xn)) + (np.sum(yn))

print(H)
