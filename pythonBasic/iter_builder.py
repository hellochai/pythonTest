#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 10:47
# @Author  : fchai
# @Desc    : 迭代器和生成器
# @File    : iter_builder.py
# @Software: PyCharm

def myrange(num: int):
    i = 0
    while i < num:
        yield i
        i += 1

class MyIterator(object):
    def __init__(self):
        pass

    def __next__(self):
        pass

if __name__ == '__main__':
    for i in myrange(10):
        print(i)
