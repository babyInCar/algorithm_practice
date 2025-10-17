
"""
宝宝和妈妈参加亲子游戏，在一个二维矩阵（N*N）的格子地图上，宝宝和妈妈抽签决定各自的位置，地图上每个格子有不同的糖果数量，部分格子有障碍物。
游戏规则是妈妈必须在最短的时间（每个单位时间只能走一步）到达宝宝的位置，路上的所有糖果都可以拿走，不能走障碍物的格子，只能上下左右走。
请问妈妈在最短到达宝宝位置的时间内最多拿到多少糖果（优先考虑最短时间到达的情况下尽可能多拿糖果）。

输入描述
第一行输入为 N，N 表示二维矩阵的大小。2 ≤ n ≤ 50
之后 N 行，每行有 N 个值，表格矩阵每个位置的值，其中：

-3：妈妈
-2：宝宝
-1：障碍
≥0：糖果数（0表示没有糖果，但是可以走）
输出描述
输出妈妈在最短到达宝宝位置的时间内最多拿到多少糖果，行末无多余空格.无法到达输入-1。

示例1
输入
4
3 2 1 -3
1 -1 1 1
1 1 -1 2
-2 1 2 3
输出
9
"""

from collections import deque


def bfs(grid, startX, startY):
    # 四个方向
    direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    n = len(grid)
    candy = [[-1] * n for _ in range(n)]
    candy[startX][startY] = 0
    q = deque()

    # 压缩二维转一维
    q.append(startX * n + startY)
    res = -1

    while q:
        # 是否到达宝宝处 标志
        flag = False
        next_queue = deque()
        while q:
            pos = q.popleft()
            x, y = divmod(pos, n)
            for dx, dy in direct:
                newX, newY = x + dx, y + dy
                # 越界
                if newX < 0 or newY < 0 or newX >= n or newY >= n:
                    continue
                # 障碍物
                if grid[newX][newY] == -1:
                    continue
                # 初次访问才能加入队列 因为要求最短路径 只考虑最短路径到达的情况
                if candy[newX][newY] == -1:
                    next_queue.append(newX * n + newY)
                # 更新candy的值
                candy[newX][newY] = max(candy[newX][newY], candy[x][y] + max(0, grid[newX][newY]))
                # 到达宝宝位置
                if grid[newX][newY] == -2:
                    res = candy[newX][newY]
                    flag = True
        if flag:
            return res
        q = next_queue
    return -1


if __name__ == "__main__":
    n = int(input())
    grid = []
    startX = startY = -1
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == -3:
                startX, startY = i, j
        grid.append(row)
    res = bfs(grid, startX, startY)
    print(res)

