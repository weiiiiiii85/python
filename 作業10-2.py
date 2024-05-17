# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:16:48 2024

@author: user
"""

import tkinter as tk
from tkinter import messagebox
import random

# 創建主視窗
root = tk.Tk()
root.title("簡易數學題目")

# 隨機生成兩個數字
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
correct_answer = num1 + num2

# 顯示題目
question_label = tk.Label(root, text=f"{num1} + {num2} = ?")
question_label.pack()

# 創建答案輸入框
answer_entry = tk.Entry(root)
answer_entry.pack()

# 定義檢查答案的函數
def check_answer():
    try:
        user_answer = int(answer_entry.get())
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
