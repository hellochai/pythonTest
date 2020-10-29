#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 10:10
# @Author  : fchai
# @Desc    :
# @File    : array_py.py
# @Software: PyCharm

from array import *

arr = array('b')
for i in  range(100):
    arr.append(i)
print(hash(arr.index(2)))

class C:
    def __init__(self):
        self.__x = None

    def __getx(self):
        r = self.__x if self.__x else None
        return r

    def __setx(self, v):self.__x = v

    def __delx(self):
        del self.__x


    x = property(fget=__getx, fset=__setx, fdel=__delx)

class C_(object):
    def __init__(self):
        self.__x = None
    @property
    def x(self):
        """I'm the `x` property"""
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @x.getter
    def x(self):
        return self.__x

    @x.deleter
    def x(self):
        del self.__x


if __name__ == '__main__':
    # c = C_()
    # c.x = 100
    # print(c.x)
    hash('ssv')
    d = dict()







