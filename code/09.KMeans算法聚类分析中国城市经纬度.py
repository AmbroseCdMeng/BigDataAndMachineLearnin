# coding=utf-8
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# with open('main.txt', 'w') as f:
#     f.write('test default file path')


# 从磁盘读取数据
X = []
with open('大数据与机器学习/code/09.China_City_Position.txt', 'r', encoding='utf-8') as f:
    for v in f:
        #print(re.findall(r'\d+\.?\d+', v.split(',')[2])[0])
        #print(re.findall(r'\d+\.?\d+', v.split(',')[3]))
        X.append([float(re.findall(r'\d+\.?\d+', v.split(',')[2])[0]),
                  float(re.findall(r'\d+\.?\d+', v.split(',')[3])[0])])


# 转换 numpy array
X = np.array(X)
print(X)

# 定义类簇数量
n_clusters = 5

# 将数据和对应的分类数放入聚类函数中进行聚类
cls = KMeans(n_clusters).fit(X)

# X 中的每项所属分类的一个列表
cls.labels_

# 画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members, 0], X[members, 1], s=60,
                marker=markers[i], c='b', alpha=0.5)

plt.title('K-Means')
plt.show()
