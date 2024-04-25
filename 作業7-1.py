# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:21:25 2024

@author: Student
"""

import random

# 姓名列表
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ivy", "Jack"]

# 隨機生成10個名字
random_names = random.sample(names, 10)

# 印出隔行的名字
for i, name in enumerate(random_names):
    if i % 2 == 0:
        print(name)
    else:
        print(name, end="\n\n")  # 使用 end="\n\n" 來隔行印出
