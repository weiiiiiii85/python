# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def truth_table():
    # 定義P和Q的可能值
    values = [True, False]

    # 列印表頭
    print("P\tQ\tResult")
    print("------------------")

    # 生成所有可能的組合
    for p in values:
        for q in values:
            # 計算結果（這裡可以修改為你的邏輯表達式）
            result = p and q

            # 列印每一行的數據
            print(f"{p}\t{q}\t{result}")

# 執行真值表函數
truth_table()
