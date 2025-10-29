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


def bfs(matrix, startX,startY,targetX, targetY):

    directions = [(0, 1), (0,-1), (-1,0), (1,0)]  # 宝妈前进的方向

    max_candy = [[-1]*N for _ in range(N)]
    dist = [[-1] * N for _ in range(N)] # 记录到达该坐标的步数

    start_p = deque()
    start_p.append(tuple(mom_base))
    max_candy[startX][startY] = 0
    # target_x, target_y = child_base[0][0], child_base[0][1]
    # candy_count = 0

    min_steps = -1  #
    found = False

    while start_p:
        x, y = start_p.popleft()

        # 如果已经找到孩子，并且节点数超过最短步数，无需继续处理
        if found and dist[x][y] > min_steps:
            break

        for dx, dy in directions:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != -1:
                # 计算新步数和新糖果总数
                new_step = dist[x][y] + 1
                new_candy = max_candy[x][y] + (matrix[nx][ny] if matrix[nx][ny] != -2 else 0)

                # 分两种情况,情况1：该节点未访问过
                if dist[nx][ny] == -1:
                    dist[nx][ny] = new_step
                    max_candy[nx][ny] = new_candy
                    start_p.append((nx, ny))
                    if matrix[nx][ny] == -2:
                        found = True
                        min_steps = new_step
                # 情况2：该节点已访问，且步数相同->更新最大糖果数(不加入队列)
                elif dist[nx][ny] == new_step:
                    if new_candy > max_candy[nx][ny]:
                        max_candy[nx][ny] = new_candy
                    if matrix[nx][ny] == -2:
                        found = True
                        min_steps = new_step
                # steps += 1
                # dist[nx][ny] = True
                # candy_count += matrix[nx][ny]
                # max_candy[nx][ny] = max(candy_p[nx][ny], candy_p[x][y] + max(0, matrix[nx][ny]))
                # if matrix[nx][ny] == -2:
                #     res = candy_p[nx][ny]
                #     break
    print(max_candy[targetX][targetY] if found else -1)


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    mom_base = []
    child_base = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == -3:
                mom_base = [i, j]
            elif matrix[i][j] == -2:
                child_base= [i, j]
    bfs(matrix, mom_base[0], mom_base[1], child_base[0], child_base[1])