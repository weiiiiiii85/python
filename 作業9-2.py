# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:06:54 2024

@author: user
"""

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def determine_zodiac(birthdate):
    zodiac_signs = [(1, 20, '摩羯座'), (2, 19, '水瓶座'), (3, 21, '雙魚座'), (4, 20, '白羊座'),
                    (5, 21, '金牛座'), (6, 21, '雙子座'), (7, 23, '巨蟹座'), (8, 23, '獅子座'),
                    (9, 23, '處女座'), (10, 23, '天秤座'), (11, 23, '天蠍座'), (12, 22, '射手座')]
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    for sign_date in zodiac_signs:
        if (birthdate.month, birthdate.day) <= (sign_date[0], sign_date[1]):
            return sign_date[2]

# 输入生日日期，格式为YYYY-MM-DD
birthdate = input("请输入生日日期（YYYY-MM-DD）：")
age = calculate_age(birthdate)
zodiac_sign = determine_zodiac(birthdate)
print("年龄：", age)
print("星座：", zodiac_sign)
