"""
题目描述
有一辆汽车需要从 m * n 的地图左上角（起点）开往地图的右下角（终点），去往每一个地区都需要消耗一定的油量，加油站可进行加油。

请你计算汽车确保从从起点到达终点时所需的最少初始油量。

说明：

智能汽车可以上下左右四个方向移动
地图上的数字取值是 0 或 -1 或 正整数：
-1 ：表示加油站，可以加满油，汽车的油箱容量最大为100；
0 ：表示这个地区是障碍物，汽车不能通过
正整数：表示汽车走过这个地区的耗油量
如果汽车无论如何都无法到达终点，则返回 -1
输入描述
第一行为两个数字，M，N，表示地图的大小为 M * N

0 < M,N ≤ 200
后面一个 M * N 的矩阵，其中的值是 0 或 -1 或正整数，加油站的总数不超过 200 个

输出描述
如果汽车无论如何都无法到达终点，则返回 -1

如果汽车可以到达终点，则返回最少的初始油量

输入：
4,4
10,30,30,20
30,30,-1,10
0,20,20,40
10,-1,30,40

输出：
70
"""

import heapq


def check(mid, m, n, matrix):
    dis = [[-1] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]

    dis[0][0] = mid - matrix[0][0]  # 剩余油量
    if matrix[0][0] == -1:
        dis[0][0] = 100
    elif matrix[0][0] == 0 or dis[0][0] < 0: # 初始位置是障碍物或油量无法穿过第一个
        return False

    q = [(-dis[0][0], 0, 0)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        w, x, y = heapq.heappop(q)
        w = -w
        if vis[x][y]:
            continue
        vis[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 如果没越界&且未被访问过&剩余油量可以通行
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 0 and not vis[nx][ny] and matrix[nx][ny] <= w:
                if matrix[nx][ny] == -1:
                    nw = 100
                else:
                    # 剩余油量消耗掉通行当前地点
                    nw = w - matrix[nx][ny]
                if nw > dis[nx][ny]:
                    dis[nx][ny] = nw
                    heapq.heappush(q, (-nw, nx, ny))
    print(f"vis is {vis}")
    # 看是否能到达终点
    return vis[m-1][n-1]


if __name__ == '__main__':
    rows = 4
    cols = 4
    matrix = [list(map(int, input().split(","))) for _ in range(rows)]
    left = 0
    right = 100
    ans = -1

    while left <= right:
        print(f"left is {left},right is:{right}")
        mid = (left + right) // 2
        if check(mid, rows, cols, matrix):
            # 如果能到达终点，则减少初始油量
            ans = mid
            right = mid - 1
        else:
            # 反之， 增加初始油量
            left = mid + 1
    print(ans)
    # print(bfs(matrix, rows, cols))
