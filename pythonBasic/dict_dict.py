#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 14:00
# @Author  : fchai
# @Desc    :
# @File    : dict_dict.py

'''
 给定两个字典，将字典按照key排序后将对应位置的key拼接起来，value相加
'''


def fix_dict(dict1: dict, dict2: dict):
    d_key_1 = sorted(dict1)
    d_key_2 = sorted(dict2)

    dict_new = {}
    for i in range(len(d_key_1)):
        dict_new[d_key_1[i] + d_key_2[i]] = dict1[d_key_1[i]] + dict2[d_key_2[i]]

    return dict_new


if __name__ == '__main__':
    dict_1 = {'a': 1, 'c': 2, 'd': 3}
    dict_2 = {'h': 4, 'g': 5, 'f': 6}
    print(fix_dict(dict_1, dict_2))
