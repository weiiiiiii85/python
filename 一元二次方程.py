# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cmath

def quadratic_solver(a, b, c):
    # 計算判別式
    discriminant = b**2 - 4*a*c

    # 虛數解
    if discriminant < 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    # 實數解
    else:
        root1 = (-b + (discriminant**0.5)) / (2*a)
        root2 = (-b - (discriminant**0.5)) / (2*a)

    return root1, root2

# 設定 a, b, c
a = float(input("輸入a的值："))
b = float(input("輸入b的值："))
c = float(input("輸入c的值："))

# 解方程式
result = quadratic_solver(a, b, c)

# 輸出結果
print(f"方程式 {a}x^2 + {b}x + {c} = 0 的解為：")
print(f"根1: {result[0]}")
print(f"根2: {result[1]}")
