# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:06:02 2024

@author: user
"""

import random

def generate_invoice_numbers():
    # 產生特別獎、特獎、頭獎號碼
    special_prize = random.randint(10000000, 99999999)
    grand_prize = random.randint(10000000, 99999999)
    first_prizes = [random.randint(10000000, 99999999) for _ in range(3)]
    
    # 產生增開六獎號碼
    additional_sixth_prizes = [random.randint(1000, 9999) for _ in range(3)]

    return special_prize, grand_prize, first_prizes, additional_sixth_prizes

def print_invoice_numbers(month, special_prize, grand_prize, first_prizes, additional_sixth_prizes):
    print(f"{month} 月電子發票中獎號碼：")
    print(f"特別獎：{special_prize}")
    print(f"特獎：{grand_prize}")
    print("頭獎：")
    for prize in first_prizes:
        print(prize)
    print("增開六獎：")
    for prize in additional_sixth_prizes:
        print(prize)

# 11 月中獎號碼
nov_special_prize, nov_grand_prize, nov_first_prizes, nov_additional_sixth_prizes = generate_invoice_numbers()
print_invoice_numbers("11", nov_special_prize, nov_grand_prize, nov_first_prizes, nov_additional_sixth_prizes)
print()

# 12 月中獎號碼
dec_special_prize, dec_grand_prize, dec_first_prizes, dec_additional_sixth_prizes = generate_invoice_numbers()
print_invoice_numbers("12", dec_special_prize, dec_grand_prize, dec_first_prizes, dec_additional_sixth_prizes)
