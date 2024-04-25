# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:21:26 2024

@author: Student
"""

import random
import string

# 隨機生成10個 Gmail 地址
def generate_gmail():
    domains = ["gmail.com"]  # Gmail 的郵箱後綴
    letters = string.ascii_lowercase  # 小寫字母

    # 隨機生成郵箱用戶名
    username_length = random.randint(5, 10)  # 用戶名長度為5到10個字元
    username = ''.join(random.choice(letters) for _ in range(username_length))

    # 隨機選擇後綴
    domain = random.choice(domains)

    # 組合成完整的郵箱地址
    gmail_address = f"{username}@{domain}"
    return gmail_address

# 印出隔行的郵箱地址
for i in range(10):
    gmail = generate_gmail()
    print(gmail)
    if i < 9:
        print()  # 隔行印出，除了最後一行外都插入空行
