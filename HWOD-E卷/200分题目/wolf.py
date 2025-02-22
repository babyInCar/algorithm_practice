
"""
狼和羊过河
羊、狼、农夫都在岸边，当羊的数量小于狼的数量时，狼会攻击羊，农夫则会损失羊。农夫有一艘容量固定的船，能够承载固定数量的动物。

要求求出不损失羊情况下将全部羊和狼运到对岸需要的最小次数。

只计算农夫去对岸的次数，回程时农夫不会运送羊和狼。

备注：农夫在或农夫离开后羊的数量大于狼的数量时狼不会攻击羊。

输入描述
第一行输入为M，N，X， 分别代表羊的数量，狼的数量，小船的容量。

输出描述
输出不损失羊情况下将全部羊和狼运到对岸需要的最小次数（若无法满足条件则输出0）。

输入示例：
5 3 3
输出：
3

"""

from collections import deque


def is_valid(state, capacity):
    left_sheep, left_wolves, right_sheep, right_wolves = state
    # 检查左右两岸羊和狼的数量是否合法
    if left_sheep < 0 or left_wolves < 0 or right_sheep < 0 or right_wolves < 0:
        return False
    # 检查左岸羊和狼的数量关系
    if 0 < left_sheep < left_wolves:
        return False
    # 检查右岸羊和狼的数量关系
    if 0 < right_sheep < right_wolves:
        return False
    # 检查运送的动物数量是否超过船的容量
    if left_sheep + left_wolves + right_sheep + right_wolves > 0:
        if left_sheep + left_wolves - (right_sheep + right_wolves) <= capacity:
            return True
    return False


def min_crossing_times(sheep, wolves, capacity):
    # 初始状态：左岸有所有羊和狼，右岸没有羊和狼
    start_state = (sheep, wolves, 0, 0)
    # 目标状态：右岸有所有羊和狼，左岸没有羊和狼
    target_state = (0, 0, sheep, wolves)
    # 队列用于广度优先搜索
    queue = deque([(start_state, 0)])
    # 记录已经访问过的状态
    visited = set(start_state)

    while queue:
        current_state, times = queue.popleft()
        left_sheep, left_wolves, right_sheep, right_wolves = current_state

        # 到达目标状态，返回最小次数
        if current_state == target_state:
            return times

        # 尝试所有可能的运送组合
        for s in range(min(left_sheep + 1, capacity + 1)):
            for w in range(min(left_wolves + 1, capacity - s + 1)):
                if 0 < s + w <= capacity:
                    new_left_sheep = left_sheep - s
                    new_left_wolves = left_wolves - w
                    new_right_sheep = right_sheep + s
                    new_right_wolves = right_wolves + w
                    new_state = (new_left_sheep, new_left_wolves, new_right_sheep, new_right_wolves)

                    # 检查新状态是否合法且未被访问过
                    if is_valid(new_state, capacity) and new_state not in visited:
                        visited.add(new_state)
                        print(f"time is:{times}")
                        queue.append((new_state, times + 1))

    return 0

# # 读取输入
# sheep, wolves, capacity = map(int, input().split())
# # 计算最小过河次数
# result = min_crossing_times(sheep, wolves, capacity)
# print(result)


if __name__ == '__main__':
    # M, N, X = map(int, input().split())
    print("=======")
    m, n, vol = map(int, input().split(","))
    print(min_crossing_times(m, n, vol))
