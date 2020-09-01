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
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
import numpy as np


film_data = open("films.csv", "rt")
reader = csv.reader(film_data)

# 表头信息
headers = next(reader)
print(headers)


feature_list = []
result_list = []
for row in reader:
    # print("row: ", row[-1])
    result_list.append(row[-1])

    # 去掉首位两列，特征集中只保留type, country, gross
    feature_list.append(dict(zip(headers[1:-1], row[1:-1])))

# print(result_list)
# print(feature_list)

vec = DictVectorizer()
dummyX = vec.fit_transform(feature_list).toarray()
dummyY = preprocessing.LabelBinarizer().fit_transform(result_list)

print("dummpyX \n", dummyX)
print("dummpyY \n", dummyY)

clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
clf = clf.fit(dummyX, dummyY)
print('clf' + str(clf))


import os

ospath = os.path

os.environ['PATH'] += os.pathsep + r'E:\Tools\Graphviz\bin'
dot_data = tree.export_graphviz(clf
                                ,feature_names=vec.get_feature_names()
                                ,filled=True
                                ,rounded=True
                                ,out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
print(type(graph))
graph.write_pdf('film.pdf')

