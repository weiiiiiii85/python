# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:37:51 2024

@author: user
"""

# 建立字典
letter_dict = {chr(97+i): chr(65+i) for i in range(26)}

# 使用者輸入
user_input = input("請輸入小寫英文字母：")

# 將輸入轉換為大寫
uppercased_input = ''.join([letter_dict.get(char, char) for char in user_input])

# 顯示結果
print("轉換後的結果為：", uppercased_input)
