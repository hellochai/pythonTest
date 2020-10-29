#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 16:08
# @Author  : fchai
# @Desc    :
# @File    : judge_data.py
# @Software: PyCharm

'''
给定一个二维数组，每一行从左往右递增排序，从上往下递增排序
给定一个数，判断这个数是否在该二维数组中

[
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]
]

Given target=5, return True
Given target=20, return False
'''


class Solution:
    # array二维表
    def Find(self, target, array):
        if array == []:
            return False
        num_row = len(array)
        num_col = len(array[0])

        i = num_col - 1
        j = 0

        while i >= 0 and j < num_row:
            if array[j][i] > target:
                i -= 1
            elif array[j][i] < target:
                j += 1
            else:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    array = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(s.Find(1, array))
