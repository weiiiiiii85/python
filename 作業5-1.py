# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:00:38 2024

@author: user
"""

def print_pattern(n):
    for i in range(1, n + 1):
        # 打印空格
        for j in range(n - i):
            print(" ", end="")
        
        # 打印左半部分的數字
        for j in range(i, 0, -1):
            print(j, end="")
        
        # 打印右半部分的數字
        for j in range(2, i + 1):
            print(j, end="")
        
        print()

# 調用函數，傳入10作為最大數字
print_pattern(10)