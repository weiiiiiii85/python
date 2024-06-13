# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:37:47 2024

@author: user
"""

import pandas as pd
import numpy as np

# 假設學號數字為12345678
student_number = 12345678

# (a) 顯示學號數字10進位
print(student_number)

# (b) 顯示學號數字8進位
print(oct(student_number))

# (c) 顯示學號數字2進位
print(bin(student_number))

# (d) 顯示學號數字16進位制，資料型態為數字
print(hex(student_number))

# (e) 顯示學號數字16進位制，資料型態為字串
print(str(hex(student_number)))

# (f) 學號數字右對齊並填充空位20格
print(f"{student_number: >20}")

# (g) 圓周率π保留小數點後面六位有效數字
pi_value = np.pi
print(f"{pi_value:.6f}")

# (h) 自然指數e保留小數點後面六位有效數字，整數部位補5個0
e_value = np.e
print(f"{e_value:010.6f}")

# (i) 輸出e^π，保留3位小數位，空白補3個0
e_pow_pi = np.exp(np.pi)
print(f"{e_pow_pi:0.3f}")

# (j) 將以上print結果存成excel
data = {
    "Description": [
        "Student Number (Decimal)",
        "Student Number (Octal)",
        "Student Number (Binary)",
        "Student Number (Hexadecimal - Number)",
        "Student Number (Hexadecimal - String)",
        "Right aligned Student Number",
        "Pi (6 decimal places)",
        "e (6 decimal places, leading zeros)",
        "e^π (3 decimal places)"
    ],
    "Value": [
        student_number,
        oct(student_number),
        bin(student_number),
        hex(student_number),
        str(hex(student_number)),
        f"{student_number: >20}",
        f"{pi_value:.6f}",
        f"{e_value:010.6f}",
        f"{e_pow_pi:0.3f}"
    ]
}

df = pd.DataFrame(data)
df.to_excel("student_info.xlsx", index=False)
