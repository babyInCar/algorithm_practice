"""
题目描述
孙悟空爱吃蟠桃，有一天趁着蟠桃园守卫不在来偷吃。已知蟠桃园有 N 棵桃树，每颗树上都有桃子，守卫将在 H 小时后回来。

孙悟空可以决定他吃蟠桃的速度K（个/小时），每个小时选一颗桃树，并从树上吃掉 K 个，如果树上的桃子少于 K 个，则全部吃掉，并且这一小时剩余的时间里不再吃桃。

孙悟空喜欢慢慢吃，但又想在守卫回来前吃完桃子。

请返回孙悟空可以在 H 小时内吃掉所有桃子的最小速度 K（K为整数）。如果以任何速度都吃不完所有桃子，则返回0。

输入描述
一行输入为 N 个数字，N 表示桃树的数量，这 N 个数字表示每颗桃树上蟠桃的数量。

第二行输入为一个数字，表示守卫离开的时间 H。

其中数字通过空格分割，N、H为正整数，每颗树上都有蟠桃，且 0 < N < 10000，0 < H < 10000。

输出描述
吃掉所有蟠桃的最小速度 K，无解或输入异常时输出 0。

输入示例:
30 11 23 4 20
6

输出示例：
23
"""

from math import ceil
def can_eat_all(peaches, speed, hours):
    hours_need = sum(ceil(p/speed) for p in peaches)
    return hours_need < hours

def min_hours_eat_all(peaches, hours):
    if len(peaches) > hours:
        return 0
    left, right = 1, max(peaches)
    mid = (left + right) // 2
    while left < right:
        if can_eat_all(peaches, mid, hours):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    peaches = list(map(int, input().split(" "))
    hours = int(input())
    cost = min_hours_eat_all(peaches, hours)
    print(cost)
   
