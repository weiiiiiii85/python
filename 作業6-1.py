# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:41:11 2024

@author: Student
"""

import random

def monte_carlo_estimate_circle_area(num_samples):
    count_inside = 0
    
    for _ in range(num_samples):
        # 在正方形內隨機生成一個點的座標 (x, y)，範圍是[-1, 1] × [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # 計算點到原點的距離
        distance = (x ** 2 + y ** 2) ** 0.5
        
        # 檢查點是否在單位圓內
        if distance <= 1:
            count_inside += 1
    
    # 單位圓面積的估計值 = (落在圓內的點數 / 總點數) × 正方形面積
    square_area = 4  # 外接正方形的面積是 2 × 2 = 4
    estimated_circle_area = (count_inside / num_samples) * square_area
    
    return estimated_circle_area

# 設定抽樣數量，可以根據需要調整
num_samples = 1000000

# 使用蒙地卡羅方法估計單位圓的面積
estimated_area = monte_carlo_estimate_circle_area(num_samples)

# 顯示結果
print(f"單位圓面積的估計值為: {estimated_area}")