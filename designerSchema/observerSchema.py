#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 11:25
# @Author  : fchai
# @Desc    : 观察者模式
# @File    : observerSchema.py
# @Software: PyCharm


class Subject:
    def  __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            # 可以设置过滤条件，对不符合过滤条件的更新
            if modifier != observer:
                observer.update(self)

class File(Subject):
    def __init__(self, file_dict):
        super(File, self).__init__()
        self._file_dict = file_dict

    @property
    def file_dict(self):
        return self._file_dict

    @file_dict.setter
    def file_dict(self, dic):
        return self._file_dict

    def add(self, key, value):
        self.file_dict[key] = value
        self.notify()

    def delete(self, key):
        self.file_dict.pop(key)
        self.notify()

    # 更换value
    def change_value(self, key, value):
        self.file_dict[key] = value
        self.notify()

class MainFrameFileDictView:
    def update(self, subject):
        print("Edit Frame:" + str(subject.file_dict))

class OriginFrameFileDictView:
    def update(self, subject):
        print("Origin Frame: "  + str(subject.file_dict))

if __name__ == '__main__':
    file_dict_1 = {0: 'lily', 1: 'ben', 2: 'jack'}
    file = File({})
    edit_view = MainFrameFileDictView()

    origin_view = OriginFrameFileDictView()
    file.attach(edit_view) # 将edit_view加入观察列表
    file.attach(origin_view) # ..

    file.file_dict = file_dict_1
    file.add(3, 'kkw')


