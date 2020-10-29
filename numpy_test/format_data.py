#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 16:12
# @Author  : fchai
# @Desc    :
# @File    : format_data.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host='192.168.1.14', port=7000, user='root', password='dhlktech',database='standard_light')

sql = """select part_num, addr_num, short_addr from light_info"""
cursor = conn.cursor()
cursor.execute(sql)
data = cursor.fetchall()

s = ""
count = 0
for d in data:
    s += '"'+ str(d[0])+str(d[1]) + '"'+ ":"+ '"' + ("00000000"+hex(int(d[2]))[2:])[-8:] +'"' + ","
    count += 1

print(s.lower())
print(count)













