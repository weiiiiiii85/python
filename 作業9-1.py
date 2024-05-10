# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:06:55 2024

@author: user
"""

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# 输入生日日期，格式为YYYY-MM-DD
birthdate = input("请输入生日日期（YYYY-MM-DD）：")
age = calculate_age(birthdate)
print("年龄：", age)
