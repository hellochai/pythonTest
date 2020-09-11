#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 17:38
# @Author  : fchai
# @Desc    :
# @File    : getToghterChildSerial.py
# @Software: PyCharm
import pydotplus
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
clf = tree.DecisionTreeClassifier(criterion='entropy'
                                  , random_state=0
                                  , splitter='random'
                                  , )
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)  # 返回预测的准确度accuracy

print("score", score)

import graphviz

featur_name = ["酒精", "苹果酸", "灰", "灰的碱性", "镁", "总酚", "类黄酮", "非黄烷类酚类", "花青素", "颜色强度",
               '色调', 'od280/od315稀释葡萄酒', '脯氨酸']

dot_data = tree.export_graphviz(clf
                                , feature_names=featur_name
                                , class_names=["琴酒", '雪莉', '贝尔摩德']
                                ,filled=True
                                ,rounded=True
                                )
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('drink.pdf')

print(clf.feature_importances_)

print([*zip(featur_name, clf.feature_importances_)])
clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)  # random_state 用来设置分支中的 随机数的模型
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print("score 2 : ", score)

import matplotlib.pyplot as plt

test = []
for i in range(10):
    clf = tree.DecisionTreeClassifier(max_depth=i + 1
                                      , criterion='entropy'
                                      , random_state=30
                                      , splitter='random')
    clf = clf.fit(Xtrain, Ytrain)
    score = clf.score(Xtest, Ytest)
    test.append(score)
plt.plot(range(1, 11), test, color='red', label='max_depth')
plt.legend()
plt.show()



