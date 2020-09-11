#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 16:16
# @Author  : fchai
# @Desc    :
# @File    : decision_tree.py
# @Software: PyCharm

# 决策数
import csv

import pydotplus as pydotplus
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
import numpy as np

# clf = clf.fit(dummyX, dummyY)
from sklearn.model_selection import train_test_split, GridSearchCV

feature_names = ['E_E','brt_ness','E_V', 'E_I']


Xtrain = ""
Xtest = ""
Ytrain = ''
Ytest = ''

with open("dhlk_light.csv", "rt") as csv_file:

    data_file = csv.reader(csv_file)
    temp = next(data_file)
    n_samples = 458668
    n_features = 4
    # target_names = np.array(temp[2:])
    data = np.empty((n_samples, n_features))
    target = np.empty((n_samples,), dtype=np.int)

    for i, ir in enumerate(data_file):
        data[i] = np.asarray(ir[3:], dtype=np.float64)
        target[i] = np.asarray(ir[1])

    Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, target, test_size=0.3)

clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=0, splitter='random')

clf.fit(Xtrain, Ytrain)


import os

ospath = os.path

os.environ['PATH'] += os.pathsep + r'E:\Tools\Graphviz\bin'
dot_data = tree.export_graphviz(clf
                                , feature_names=feature_names
                                , filled=True
                                , rounded=True
                                , out_file=None)
#


from sklearn.preprocessing import StandardScaler

# 数据标准化
data = [[-1, 2], [-0.5,6],[0,10],[1, 18]]

scaler = StandardScaler()
scaler.fit(data) # fit 本质是生成均值和方差
print("xxxxxxxxx",scaler.mean_) # 查看均值的属性mean_
print("xssss",scaler.var_) # 查看方差的属性 var_
x_std =scaler.transform(data) # 通过接口导出结果
# x_std.mean() # 导出的结果是一个数组， 用mean（）查看均值

