# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:21:25 2024

@author: Student
"""

import random

# 隨機生成10個手機號碼
def generate_phone_number():
    # 隨機生成號碼前三位（國碼）
    country_code = "+86"  # 假設是中國的國碼
    # 隨機生成後8位數字（手機號碼）
    phone_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f"{country_code} {phone_number[:4]}-{phone_number[4:]}"

# 印出隔行的手機號碼
for i in range(10):
    phone_number = generate_phone_number()
    print(phone_number)
    if i < 9:
        print()  # 隔行印出，除了最後一行外都插入空行
