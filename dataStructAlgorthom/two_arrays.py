#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 14:22
# @Author  : fchai
# @Desc    :
# @File    : two_arrays.py
# @Software: PyCharm

from arrays import Array

class Grid(object):
    '''Grid类用来表示二维数组'''
    def __init__(self, rows, columns, fillValue=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue=None)

    # 获取二维数组的行数
    def getHeight(self):
        return len(self._data)

    # 获取二维表的列数
    def getWidth(self):
        return len(self._data[0])

    # 获取二维数组指定索引处的字符串
    def __getitem__(self, rowIndex):
        return self._data[rowIndex]

    # 将二维数组转换为字符串
    def __str__(self):
        result = ''
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + ' '
            result += '\n'

        return result

if __name__ == '__main__':
    g = Grid(3, 4)
    num_rows = g.getHeight()
    num_columns = g.getWidth()
    for i in range(num_rows):
        for j in range(num_columns):
            g[i][j] = i + j

    print(g)
    print(g.__getitem__(2)[3])
    print(g.__str__())








