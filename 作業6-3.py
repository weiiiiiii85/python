# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:40:28 2024

@author: Student
"""

import random
import math

def monte_carlo_cone_surface_area(num_samples):
    total_surface_area = 0.0
    
    for _ in range(num_samples):
        # 在單位圓內隨機生成一個點的座標 (x, y)，範圍是 [-1, 1] × [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # 檢查點是否在單位圓內
        if x**2 + y**2 <= 1:
            # 點在單位圓內，計算圓錐的側面積
            r = math.sqrt(x**2 + y**2)  # 圓錐底面半徑
            l = math.sqrt(r**2 + 1)  # 圓錐斜高
            side_area = math.pi * r * l  # 圓錐側面積
            base_area = math.pi  # 圓錐底面積（單位圓面積）
            
            # 累加側面積和底面積
            total_surface_area += side_area + base_area
    
    # 計算蒙地卡羅法估算的圓錐表面積
    estimated_surface_area = total_surface_area / num_samples
    
    return estimated_surface_area

# 設定抽樣數量，可以根據需要調整
num_samples = 1000000

# 使用蒙地卡羅法估計圓錐的表面積
estimated_area = monte_carlo_cone_surface_area(num_samples)

# 顯示結果
print("圓錐的表面積的估計值為:", estimated_area)
