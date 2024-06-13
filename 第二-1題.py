# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 01:02:33 2024

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

# 設定x的範圍
x = np.linspace(-10, 10, 400)

# 建立一個3x3的子圖
fig, axes = plt.subplots(3, 3, figsize=(15, 15))

# 定義九個不同的函數
functions = [
    lambda x: x,
    lambda x: x**2,
    lambda x: x**3,
    lambda x: np.sin(x),
    lambda x: np.cos(x),
    lambda x: np.tan(x),
    lambda x: np.exp(x),
    lambda x: np.log(np.abs(x) + 1),
    lambda x: 1 / (1 + np.exp(-x))
]

# 定義每個子圖的標題
titles = [
    "y = x",
    "y = x^2",
    "y = x^3",
    "y = sin(x)",
    "y = cos(x)",
    "y = tan(x)",
    "y = exp(x)",
    "y = log(|x| + 1)",
    "y = 1 / (1 + exp(-x))"
]

# 繪製每個子圖
for i, ax in enumerate(axes.flat):
    ax.plot(x, functions[i](x))
    ax.set_title(titles[i])
    ax.grid(True)

# 調整子圖間距
plt.tight_layout()

# 顯示圖像
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 設定x的範圍
x = np.linspace(-10, 10, 400)

# 建立一個3x3的子圖
fig, axes = plt.subplots(3, 3, figsize=(15, 15))

# 定義九個不同的函數
functions = [
    lambda x: x,
    lambda x: x**2,
    lambda x: x**3,
    lambda x: np.sin(x),
    lambda x: np.cos(x),
    lambda x: np.tan(x),
    lambda x: np.exp(x),
    lambda x: np.log(np.abs(x) + 1),
    lambda x: 1 / (1 + np.exp(-x))
]

# 定義每個子圖的標題
titles = [
    "y = x",
    "y = x^2",
    "y = x^3",
    "y = sin(x)",
    "y = cos(x)",
    "y = tan(x)",
    "y = exp(x)",
    "y = log(|x| + 1)",
    "y = 1 / (1 + exp(-x))"
]

# 繪製每個子圖
for i, ax in enumerate(axes.flat):
    ax.plot(x, functions[i](x))
    ax.set_title(titles[i])
    ax.grid(True)

# 調整子圖間距
plt.tight_layout()

# 顯示圖像
plt.show()
