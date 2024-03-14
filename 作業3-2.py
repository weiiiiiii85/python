# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:38:07 2024

@author: user
"""

import random

# 使用者輸入
n = int(input("請輸入要抽取的數字個數 n："))
a = int(input("請輸入範圍起始值 a："))
b = int(input("請輸入範圍結束值 b："))

# 隨機抽取 n 個數字
random_numbers = random.sample(range(a, b+1), n)

# 刪除重複的數字並排序
random_numbers = sorted(set(random_numbers), reverse=True)

# 顯示結果
print("抽取的隨機數字（刪除重複並由大到小排序）：", random_numbers)
