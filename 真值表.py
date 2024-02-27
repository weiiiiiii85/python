# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def generate_truth_table(variables):
    num_vars = len(variables)
    table = []

    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars):
            # 將整數轉換為二進位，然後取第j位的值
            value = (i >> j) & 1
            row.append(value)
        table.append(row)

    return table

def display_truth_table(variables, truth_table):
    # 輸出表頭
    header = " | ".join(variables + ["Result"])
    print(header)
    print("-" * len(header))

    # 輸出每一行
    for row in truth_table:
        row_str = " | ".join(map(str, row))
        print(row_str)

# 設定布林變數
variables = ["A", "B", "C"]

# 生成真值表
truth_table = generate_truth_table(variables)

# 顯示真值表
display_truth_table(variables, truth_table)
