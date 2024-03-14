# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:38:07 2024

@author: user
"""

import random

# 建立一副撲克牌
suits = ['♥', '♦', '♣', '♠']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for suit in suits for rank in ranks]

# 洗牌
random.shuffle(deck)

# 發牌給四個人
player1 = []
player2 = []
player3 = []
player4 = []

for i in range(len(deck)):
    if i % 4 == 0:
        player1.append(deck[i])
    elif i % 4 == 1:
        player2.append(deck[i])
    elif i % 4 == 2:
        player3.append(deck[i])
    else:
        player4.append(deck[i])

# 對每個玩家的手牌進行排序
player1.sort(key=lambda x: ranks.index(x[0]))
player2.sort(key=lambda x: ranks.index(x[0]))
player3.sort(key=lambda x: ranks.index(x[0]))
player4.sort(key=lambda x: ranks.index(x[0]))

# 顯示結果
print("玩家1的手牌：", player1)
print("玩家2的手牌：", player2)
print("玩家3的手牌：", player3)
print("玩家4的手牌：", player4)
