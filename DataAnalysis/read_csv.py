#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 15:40
# @Author  : fchai
# @Desc    : 读csv文件
# @File    : read_csv.py
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt


file_csv = pd.read_csv("part-00000-5fc98cb6-8d10-4229-a8d3-8507a7aa0ac5-c000.csv")
print(file_csv._values)

from sklearn.cluster import KMeans

km = KMeans(n_clusters=3)
y_pre = km.fit(file_csv)

plt.scatter(file_csv[:, 2], file_csv[:, 3], c=y_pre)

plt.show()
