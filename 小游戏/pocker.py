"""写一个程序，实现发牌，比大小 判断输赢
   游戏规则：
   一副扑克牌，去掉大小王，每个玩家3张牌，最后比大小，看谁赢

    有一下几种牌：
    豹子：三张一样的牌，如3张6
    同花顺：即三张同样花色的顺子，如红桃5、6、7
    顺子：又称拖拉机，花色不同，但是顺子
    对子：2张牌一样
    单张：单张最大的是A
    这几种牌的大小顺序是：豹子>同花顺>同花>顺子>对子>单张

    需程序实现的点：
    1.先生成一付完整的扑克牌
    2.给5个玩家随机发牌
    3.统一开牌，比大小，输出赢家是谁
"""

"""
解题思路：
1.生成一副牌
2.给五个玩家随机发牌
3.设计比较大小的规则
4.给出获胜的玩家
"""
import random
from typing import List, Dict
def create_new_pocker_list() -> list:
    color_type = ['♣', '♥', '♠', '♦']
    pocker_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    pocker_list = []

    for color in color_type:
        count = 2
        for pocker in pocker_num:
            pocker_list.append([f'{color}{pocker}', count])
            count += 1
    return pocker_list
# print(create_new_pocker_list())

# Step 2.发牌
player_list = ['周润发', '李宇春', '光头佬', '四眼仔', '神经蛙']
def send_pocker_to_player(player_list: List, pocker_list: List,  pocker_num: int):
    """给玩家发牌 """
    pocker_dict = {}
    for player in player_list:
        pocker_single = random.sample(pocker_list, pocker_num)
        pocker_dict[player] = pocker_single
        print(f"为玩家【{player}】生成了牌{pocker_single}")
        for num in pocker_single:
            pocker_list.remove(num)
    return pocker_dict

pocker_list = create_new_pocker_list()
# print(send_pocker_to_player(player_list, pocker_list, pocker_num=3))


# Step 3: 给牌计算权重
def bubble_sort(pocker_list)->List:
    for i in range(len(pocker_list)):
        for j in range(len(pocker_list)-i-1):
            if pocker_list[j][1] > pocker_list[j+1][1]:
                pocker_list[j], pocker_list[j+1] = pocker_list[j+1], pocker_list[j]
    return pocker_list

def calc_single_score(pocker_dict, score):
    """计算单排的分数"""
    single_list = bubble_sort(pocker_dict)
    card_val = [x[1] for x in single_list]
    score = card_val[0] * 0.1 + card_val[1] + card_val[2] * 10
    print(f"单牌的得分为:{score}")
    return score

def calc_pair_score(p_cards, score:float=0):
    """计算对子的分数"""
    card_list = bubble_sort(p_cards)
    card_val = [i[1] for i in card_list]
    if len(set(card_val)) == 2:
        if card_val[0] == card_val[1]:  # aab
            score = (card_val[0] + card_val[1]) * 50 + card_val[2]
        else:
            score = (card_val[1] + card_val[2]) * 50 + card_val[0]
    print(f"对子计算的结果为:{score}")
    return score

pocker_dict = send_pocker_to_player(player_list, pocker_list, pocker_num=3)
# print(pocker_dict)
# print(calc_pair_score(pocker_dict))

def calc_straight_score(p_cards:Dict, score:float):
    """计算顺子的分数"""
    card_list = bubble_sort(p_cards)
    card_val = [x[1] for x in card_list]
    a, b, c = card_val
    if b-a == 1 and c - b == 1:
        score *= 100
    print(f"顺子的得分为:{score}")
    return score

def calc_same_color_score(p_cards, score):
    """计算同花的得分"""
    color_list = [x[0][0] for x in p_cards]
    if len(set(color_list)) == 1:
        score *= 1000
    print(f"同花的得分为：{score}")
    return score

def calc_flush_score(p_cards, score):
    """计算同花顺的得分"""
    card_list = bubble_sort(p_cards)
    card_val = [x[1] for x in card_list]
    color_set = {x[0][0] for x in p_cards}
    if card_val[1]-card_val[0] == 1 and card_val[2] - card_val[1] == 1 and len(color_set) == 1:
        score *= 0.1
    print(f"计算同花顺的得分为:{score}")
    return score

def calc_leopard_score(p_cards, score):
    """计算豹子的得分"""
    card_list = bubble_sort(p_cards)
    card_val = {x[1] for x in card_list}
    if len(card_val) == 1:
        score *= 10000
    print(f"计算豹子的得分为:{score}")
    return score

func_list = [
             calc_single_score,
             calc_pair_score,
             calc_straight_score,
             calc_same_color_score,
             calc_flush_score,
             calc_leopard_score]
player_score = []
for player, p_cards in pocker_dict.items():
    print(f"开始计算玩家【{player}】的牌{p_cards}")
    score = 0
    for calc_func in func_list:
        score = calc_func(p_cards, score)
    player_score.append([player, score])

winner_list = bubble_sort(player_score)
print(winner_list)
print(f"恭喜获得最后胜利的同学是:【{winner_list[-1][0]}】,得分是:{winner_list[-1][1]}")

"""
本题的难点在于：
1.如何计算各种牌的权重
2.如何判断计算权重的方法是正确的呢？我们的计算方法需要满足大一层级的牌的最小值要大于小一层级牌的最大值：比如对子的最小牌要大于单牌的最大值
3.如何判断同花、顺子、同花顺、豹子的情况
4.同花顺这种情况，不能直接*1000，因为同花和顺子分别*100了1000，同花顺这种情况再乘以10000的话，那么得出的结果会比豹子还大，所以不符合我们的规则
"""