# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:29:05 2024

@author: Student
"""

import random
import math
def monte_carlo_integration(num_samples):
    total_sum = 0.0

    for _ in range(num_samples):
        # 在 [0, 2*pi] 內生成隨機值 x
        x = random.uniform(0, 2 * math.pi)
        
        # 計算 sin(x) * e^x
        integrand_value = math.sin(x) * math.exp(x)
        
        # 將每個隨機點的函數值加總起來
        total_sum += integrand_value

    # 計算蒙地卡羅法估算的積分值
    integral_approximation = (2 * math.pi) * (total_sum / num_samples)

    return integral_approximation
if __name__ == "__main__":
    num_samples = 1000000  # 可根據需要調整抽樣數量

    integral_approximation = monte_carlo_integration(num_samples)
    
    print("蒙地卡羅法估算的積分值為:", integral_approximation)
