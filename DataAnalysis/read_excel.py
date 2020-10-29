#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:23
# @Author  : fchai
# @Desc    :
# @File    : read_excel.py
# @Software: PyCharm

# 将内容写入到excel
import pandas as pd

input_file = 'dhlk_light_area.xlsx'

data_frame = pd.read_excel(input_file, sheet_name='dhlk_light_area')
writer = pd.ExcelWriter('new.xlsx')

data_frame.to_excel(writer, sheet_name='sheet1', index=False)

import pymysql
import csv

# 连接mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, password='root', database='test', user='root')
c = conn.cursor()

input_csv = 'out_file.csv'
# 读取csv文件并更新特定的行
file_reader = csv.reader(open(input_csv, 'r', newline='', encoding='utf-8'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""insert into test_csv (field1,field2, field3,field4, field5) values (%s, %s, %s, %s, %s)""", data)

conn.commit()

import matplotlib.pyplot as plt
plt.style.use('ggplot')
