#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 16:11
# @Author  : fchai
# @Desc    :
# @File    : link_py.py
# @Software: PyCharm

# 用python实现单链表

class Node(object):
    def __init__(self, item: object):
        self.element = item
        self.next = None


# 创建单链表类
class SingleLinkList(object):
    def __init__(self):
        self.header = None # 头
        self.length = 0    # 长度

    # 判断是否为空
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    # 头部插入
    def add(self, node: Node):
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header # 头部插入，链表的头节点变为插入的节点，原来的头节点为插入节点的下一个节点
            self.header = node
        self.length += 1

    # 尾部追加
    def append(self, node: Node):
        current_node = self.header
        if self.is_empty():
            self.header = node
        else:
            while (current_node.next != None):
                current_node = current_node.next

            current_node.next = node
            self.length += 1

    # 指定位置插入
    def insert(self, node: Node, index: int):
        current_node = self.header
        if index > self.length + 1 or index <= 0:
            raise Exception("index out of range")

        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1

    # 遍历
    def travel(self):
        current_node = self.header
        if self.is_empty():
            return "None"
        else:
            for i in range(0, self.length):
                print(current_node.element, end='\n')
                current_node = current_node.next

            print("\n")

    # 排序不要交换节点的位置, 只需交换节点上的数据值
    def list_sort(self):
        for i in range(0, self.length-1):
            current_node = self.header
            for j in range(0, self.length -i - 1):
                if current_node.element > current_node.next.element:
                    temp = current_node.element
                    current_node.element = current_node.next.element
                    current_node.next.element = temp

                current_node = current_node.next

    # 按索引删除
    def delete(self, index):
        if self.is_empty():
            raise  Exception("LinkList is Empty")
        elif index <= 0 or index > self.length:
            raise Exception("Index out of range")
        else:
            if index == 1:
                self.header = self.header.next
                current_node = self.header
            elif index == 2:
                current_node = self.header
                current_node.next = current_node.next.next
            else:
                current_node = self.header
                for i in range(1, index-1):
                    current_node = current_node.next
                current_node.next = current_node.next.next

            self.length -= 1


if __name__ == '__main__':
    model = Node(1)
    model1 = Node({'1': 'A', '2': "B"})
    model2 = Node([1,2,3,4])
    model3 = Node((1,2,3,4,5))

    # 创建一个单链表对象
    single_link_list = SingleLinkList()
    single_link_list.add(model)
    single_link_list.add(model1)
    single_link_list.add(model2)
    single_link_list.add(model3)

    single_link_list.travel()














