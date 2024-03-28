def print_pattern(n):
    # 計算最大行數
    max_width = 2 * n - 1

    # 上半部分
    for i in range(1, n):
        # 計算每行的空格數
        spaces = max_width - 2 * i + 1

        # 打印空格
        print(" " * (spaces // 2), end="")

        # 左半部分數字
        for j in range(1, i + 1):
            print(j, end="")

        # 右半部分數字
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()

    # 最後一行
    # 計算每行的空格數
    spaces = max_width - 2 * n + 1

    # 打印空格
    print(" " * (spaces // 2), end="")

    # 左半部分數字
    for j in range(1, n + 1):
        print(j, end="")

    # 右半部分數字
    for j in range(n - 1, 0, -1):
        print(j, end="")

    print()

# 呼叫函式，傳入10作為最大數字
print_pattern(10)
