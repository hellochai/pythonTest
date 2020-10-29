#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 18:05
# @Author  : fchai
# @Desc    :
# @File    : pic_base64.py
# @Software: PyCharm

import base64

with open(r"F:\Demo\PythonTest\pythonTest\node-red-icon.ico", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('data:image/jpeg;base64,%s' % s)
