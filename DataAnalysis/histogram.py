#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:39
# @Author  : fchai
# @Desc    :
# @File    : histogram.py.py
# @Software: PyCharm


import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15

x1 = mu1 + sigma* np.random.randn(1000)
x2 = mu2 + sigma* np.random.randn(1000)
plot_data1 = np.random.randn(50).cumsum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot()