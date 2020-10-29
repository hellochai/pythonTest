#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 15:10
# @Author  : fchai
# @Desc    :
# @File    : write_as_csv.py.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import csv

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
path = 'dhlk_basic_product_devices.csv'
data_frame = pd.read_csv(path, header=None, names=header_list)
data_frame.to_csv('out_file.csv', index=False)


