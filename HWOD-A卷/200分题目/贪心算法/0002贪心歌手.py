"""
一个歌手准备从A城去B城参加演出。
按照合同，他必须在 T 天内赶到
歌手途经 N 座城市
歌手不能往回走
每两座城市之间需要的天数都可以提前获知。
歌手在每座城市都可以在路边卖唱赚钱。
经过调研，歌手提前获知了每座城市卖唱的收入预期： 如果在一座城市第一天卖唱可以赚M，后续每天的收入会减少D（第二天赚的钱是 M - D，第三天是 M - 2D ...）。如果收入减少到 0 就不会再少了。
歌手到达后的第二天才能开始卖唱。如果今天卖过唱，第二天才能出发。

贪心的歌手最多可以赚多少钱？

输入描述
第一行两个数字T和N，中间用空格隔开。
T 代表总天数，0 < T < 1000
N 代表路上经过 N 座城市，0 < N < 100
第二行 N+1 个数字，中间用空格隔开。代表每两座城市之间耗费的时间。

其总和 ≤ T。
接下来 N 行，每行两个数字 M 和 D，中间用空格隔开。代表每个城市的输入预期。

0 < M < 1000
0 < D < 100
输出描述
一个数字。代表歌手最多可以赚多少钱。以回车结束。

示例1
输入
10 2
1 1 2
120 20
90 10
输出
540
"""

import heapq


def maximumProfit(T, N, travel_costs, city_info):
    """计算歌手的最大收益"""

    # 演出可以使用的天数
    remaining_days = T - sum(travel_costs)
    if remaining_days < 0:
        return 0

    # 取负数实现大顶堆
    pq = []
    for i, (M, _) in enumerate(city_info):
        heapq.heappush(pq, (-M, i))

    res = 0
    while remaining_days > 0:
        income, decrease = heapq.heappop(pq)
        income = -income
        res += income
        # 更新下一天收入确保不小于0，并重新入队
        new_income = max(0, income - city_info[decrease][1])
        heapq.heappush(pq, (-new_income, decrease))
        remaining_days -= 1
    return res


if __name__ == '__main__':
    T, N = map(int, input().split())
    travel_costs = [int(i) for i in input().split()]
    profit_map = {}
    city_info = []
    for i in range(N):
        M, D = map(int, input().split())
        # profit_map[M] = D
        city_info.append((M, D))
    print(maximumProfit(T, N, travel_costs, city_info))