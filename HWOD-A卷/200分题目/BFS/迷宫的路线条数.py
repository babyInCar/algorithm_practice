"""


"""

from collections import deque


def count_routes():
    # 读取输入
    X, Y = map(int, input().split())  # X：横向坐标范围(0~X-1)，Y：纵向坐标范围(0~Y-1)
    wall_num = int(input())
    # 初始化矩阵：0=普通方格，-1=墙壁
    matrix = [[0 for _ in range(Y)] for _ in range(X)]
    for _ in range(wall_num):
        x, y = map(int, input().split())
        matrix[x][y] = -1  # 标记墙壁

    # 第一步：正向BFS标记从(0,0)可达的方格（避免统计无效路径）
    reachable = [[False for _ in range(Y)] for _ in range(X)]
    forward_dirs = [(1, 0), (0, 1)]  # 仅向东（x+1）、向北（y+1）
    q = deque()

    # 起点(0,0)若不是墙壁则初始化
    if matrix[0][0] != -1:
        q.append((0, 0))
        reachable[0][0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in forward_dirs:
            nx = x + dx
            ny = y + dy
            # 边界校验 + 未访问 + 非墙壁
            if 0 <= nx < X and 0 <= ny < Y and not reachable[nx][ny] and matrix[nx][ny] != -1:
                reachable[nx][ny] = True
                q.append((nx, ny))

    # 第二步：动态规划统计路线数
    dp = [[0 for _ in range(Y)] for _ in range(X)]
    # 起点初始化：1条路线
    dp[0][0] = 1 if reachable[0][0] else 0

    # 填充第一行（y=0，只能从左边过来）
    for x in range(1, X):
        if reachable[x][0] and matrix[x][0] != -1:
            dp[x][0] = dp[x - 1][0]

    # 填充第一列（x=0，只能从下边过来）
    for y in range(1, Y):
        if reachable[0][y] and matrix[0][y] != -1:
            dp[0][y] = dp[0][y - 1]

    # 填充其他方格（可从左边或下边过来）
    for x in range(1, X):
        for y in range(1, Y):
            if reachable[x][y] and matrix[x][y] != -1:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

    # 输出终点的路线数（题目保证可达，无需处理0的情况）
    print(dp[X - 1][Y - 1])


if __name__ == '__main__':
    count_routes()