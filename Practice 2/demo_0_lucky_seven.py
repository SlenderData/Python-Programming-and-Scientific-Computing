# 赌场中有一种称为“幸运7”的游戏，游戏规则：
# 玩家掷两枚骰子，如果其点数和为7，玩家赢4元；
# 不是7，玩家就输1元。
# 现玩家有10元，当全部输掉时游戏结束，请你编程模拟之。

import random

round = 0  # 游戏轮数
player_money = 10  # 玩家初始资金
dice1 = [1, 2, 3, 4, 5, 6]  # 骰子1点数
dice2 = [1, 2, 3, 4, 5, 6]  # 骰子2点数
while player_money > 0:
    round += 1
    print("\n第%d轮：" % round)
    dice1_point = random.choice(dice1)  # 骰子1点数
    dice2_point = random.choice(dice2)  # 骰子2点数
    point = dice1_point + dice2_point  # 两枚骰子点数和
    print("骰子1点数：%d，骰子2点数：%d，点数和：%d" % (dice1_point, dice2_point, point))
    if point == 7:
        player_money += 4
        print("玩家赢了！玩家当前资金：%d" % player_money)
    else:
        player_money -= 1
        print("玩家输了！玩家当前资金：%d" % (player_money))
print("\n游戏结束！玩家输光了所有资金！")
