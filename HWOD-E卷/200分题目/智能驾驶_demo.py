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
from collections import deque


def bfs(matrix, rows, cols):

    # 定义四个方向: 上、下、左、右
    directions = [(-1,0), (1,0), (0, -1), (0, 1)]

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    ans = 0  # 需要的油量
    available = 100

    while queue:
        print(f"===={queue}")
        x, y = queue.popleft()
        gas = 0
        if matrix[x][y] > 0:
            if gas == 0:
                ans += matrix[x][y]
            if ans > 100 or available < 0: # 永远到不了终点
                return -1
            if gas >= matrix[x][y]:
                gas -= matrix[x][y]
            elif gas > 0:
                ans += (matrix[x][y] - gas)
            available -= matrix[x][y]
        elif matrix[x][y] == -1:
            gas += 100
            available += 100

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                # 检查高度差是否在允许范围内
                if matrix[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return ans


if __name__ == '__main__':
    rows = 4
    cols = 4
    matrix = [list(map(int, input().split(","))) for _ in range(rows)]
    print(bfs(matrix, rows, cols))
