# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:37:49 2024

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

# 設定隨機生成點的數量
num_points = 100000

# 隨機生成點的x和y座標
x = np.random.uniform(0, 1, num_points)
y = np.random.uniform(0, 1, num_points)

# 計算距離原點的距離
distances = np.sqrt(x**2 + y**2)

# 判斷點是否在圓內
inside_circle = distances <= 0.5

# 計算圓內點的比例
pi_estimate = np.sum(inside_circle) / num_points * 4

# 顯示結果
print(f"估計的圓周率值: {pi_estimate}")

# 畫圖顯示結果
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Monte Carlo Simulation for Estimating Pi')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# 設定隨機生成點的數量
num_points = 100000

# 隨機生成點的x和y座標
x = np.random.uniform(0, 1, num_points)
y = np.random.uniform(0, 1, num_points)

# 計算距離原點的距離
distances = np.sqrt(x**2 + y**2)

# 判斷點是否在圓內
inside_circle = distances <= 0.5

# 計算圓內點的比例
pi_estimate = np.sum(inside_circle) / num_points * 4

# 顯示結果
print(f"估計的圓周率值: {pi_estimate}")

# 畫圖顯示結果
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Monte Carlo Simulation for Estimating Pi')
plt.legend()
plt.show()
