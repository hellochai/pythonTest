#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 14:16
# @Author  : fchai
# @Desc    :
# @File    : k-means_test.py
# @Software: PyCharm


import numpy as np
import pandas as pd


import matplotlib.pyplot as plt


# 距离度量函数
def calc_disttance(vec1, vec2):
    return np.sqrt(sum(np.power(vec1 - vec2, 2)))


# 创建初始聚类中心
def create_centorid(data, k):
    centroids = np.zeros((k, n))
    centroids[0, 0] = 2
    centroids[0, 1] = 5
    centroids[1, 0] = 8
    centroids[1, 1] = 4
    centroids[2, 0] = 1
    centroids[2, 1] = 2

    return centroids


# k-means聚类
def kMeans(data, k, dist=calc_disttance, create_center=create_centorid):
    # 初始化cluster_assment,存储中间结果
    # 第一列存储索引， 第二列存储距离
    # 样本个数
    m = np.shape(data)[0]
    init = np.zeros((m, 2))
    cluster_assment = np.mat(init)

    # 初始化聚类中心矩阵
    centroids = create_center(data, k)
    for epoch in range(1):
        # 对数据集中每个样本点进行计算
        for i in range(m):
            min_distance = np.inf
            min_index = -1
            # 对将每个样本到每个中心的距离进行计算
            for j in range(k):
                dist_ij = calc_disttance(centroids[j, :], data[i, :])
                # 找到距离最近的中心的距离和索引
                if dist_ij < min_distance:
                    min_distance = dist_ij
                    min_index = j
                    cluster_assment[i:, :] = min_index, min_distance

        # 对所有节点聚类之后，重新更新中心
        for i in range(k):
            pts_in_cluster = data[np.nonzero(cluster_assment[:, 0].A == i)[0]]
            centroids[i, :] = np.mean(pts_in_cluster, axis=0)

    return centroids, cluster_assment


if __name__ == '__main__':
    data = np.array([
        [2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]
    ])

    k = 3  # 聚类个数
    n = 2  # 特征个数
    from sklearn.cluster import KMeans
    sse = []
    for i in range(1, 9):
        mid = KMeans(n_clusters=i, init='random', n_init=10,max_iter=200)

        mid.fit(data)
        sse.append(mid.inertia_)

    plt.plot(range(1, 9), sse, marker='o')
    plt.xlabel("k")
    plt.ylabel("SSE")
    plt.show()

    # centosids, cluster_assment = kMeans(data, k, dist=calc_disttance, create_center=create_centorid)
    # predict_label = cluster_assment[:, 0]
    # data_and_pred = np.column_stack((data, predict_label))

    # df
    # df = pd.DataFrame(data_and_pred, columns=['data1', 'data2', 'pred'])
    #
    # print(df)
    # df0 = df[df.pred == 0].values
    # df1 = df[df.pred == 1].values
    # df2 = df[df.pred == 2].values
    #

    #
    # # 画图
    # plt.scatter(df0[:, 0], df0[:, 1], c='turquoise',
    #             marker='o', label='label0')
    # plt.scatter(df1[:, 0], df1[:, 1], c='green',
    #             marker='*', label='label1')
    # plt.scatter(df2[:, 0], df2[:, 1], c='blue',
    #             marker='+', label='label2')
    #
    # plt.scatter(centosids[:, 0].tolist(), centosids[:, 1].tolist())
    # plt.legend(loc=2)
    # plt.show()


