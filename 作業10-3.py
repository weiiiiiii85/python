# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:16:49 2024

@author: user
"""

import tkinter as tk
from tkinter import messagebox
import random

# 創建主視窗
root = tk.Tk()
root.title("簡易數學題目")

# 定義運算符號
operators = ['+', '-', '*', '/']

# 隨機生成兩個數字和一個運算符
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
operator = random.choice(operators)

# 計算正確答案
if operator == '+':
    correct_answer = num1 + num2
elif operator == '-':
    correct_answer = num1 - num2
elif operator == '*':
    correct_answer = num1 * num2
elif operator == '/':
    if num2 != 0:
        correct_answer = num1 / num2
    else:
        correct_answer = "無效"  # 避免除以零的情況

# 顯示題目
question_label = tk.Label(root, text=f"{num1} {operator} {num2} = ?")
question_label.pack()

# 創建答案輸入框
answer_entry = tk.Entry(root)
answer_entry.pack()

# 定義檢查答案的函數
def check_answer():
    try:
        user_answer = float(answer_entry.get())
        if user_answer == correct_answer:
            messagebox.showinfo("結果", "正確！")
        else:
            messagebox.showinfo("結果", f"錯誤，正確答案是 {correct_answer}")
    except ValueError:
        messagebox.showerror("錯誤", "請輸入數字！")

# 創建提交答案的按鈕
submit_button = tk.Button(root, text="提交答案", command=check_answer)
submit_button.pack()

# 運行主循環
root.mainloop()
