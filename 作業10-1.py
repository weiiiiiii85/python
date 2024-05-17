# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:16:46 2024

@author: user
"""

import tkinter as tk
from tkinter import messagebox

# 創建主視窗
root = tk.Tk()
root.title("密碼驗證")

# 創建密碼輸入框和標籤
password_label = tk.Label(root, text="請輸入密碼：")
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# 定義檢查密碼的函數
def check_password():
    password = password_entry.get()
    if password == "12345":  # 假設密碼是"12345"
        messagebox.showinfo("結果", "密碼正確！")
    else:
        messagebox.showerror("錯誤", "密碼錯誤！")

# 創建提交密碼的按鈕
check_password_button = tk.Button(root, text="提交密碼", command=check_password)
check_password_button.pack()

# 運行主循環
root.mainloop()
