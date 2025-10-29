"""
房间由XY的方格组成，例如下图为6*4的大小。每一个方格以坐标(x，y)描述。
机器人固定从方格(0，0)出发，只能向东或者向北前进。出口固定为房间的最东北角，如下图的方格(5，3)。用例保证机器人可以从入口走到出口。
房间有些方格是墙壁，如(4，1)，机器人不能经过那儿。
有些地方是一旦到达就无法走到出口的，如标记为B的方格，称之为陷阱方格。
有些地方是机器人无法到达的的，如标记为A的方格，称之为不可达方格，不可达方格不包括墙壁所在的位置。
如下示例图中，陷阱方格有2个，不可达方格有3个。
请为该机器人实现路径规划功能：给定房间大小、墙壁位置，请计算出陷阱方格与不可达方格分别有多少个。
输入描述
第一行为房间的X和Y（0 < X,Y <= 1000）
第二行为房间中墙壁的个数N（0 <= N < X*Y）
接着下面会有N行墙壁的坐标
同一行中如果有多个数据以一个空格隔开，用例保证所有的输入数据均合法。（结尾不带回车换行）

输出描述
陷阱方格与不可达方格数量，两个信息在一行中输出，以一个空格隔开。（结尾不带回车换行）


输入描述
第一行为房间的X和Y（0 < X,Y <= 1000）
第二行为房间中墙壁的个数N（0 <= N < X*Y）
接着下面会有N行墙壁的坐标
同一行中如果有多个数据以一个空格隔开，用例保证所有的输入数据均合法。（结尾不带回车换行）

输出描述
陷阱方格与不可达方格数量，两个信息在一行中输出，以一个空格隔开。（结尾不带回车换行）

用例1
输入
6 4
5
0 2
1 2
2 2
4 1
5 1

输出：
2 3

思路：
1.把墙的位置初始化为-1，其它位置初始化为0
2.通过BFS遍历，如果能到达终点，则把通过的点置为1，不能通过的路线，把通过的点置为2
3.统计0的数量为不可到达的个数，统计1的数量为陷阱个数
"""


from collections import deque


def bfs():

    row, column = map(int, input().split())
    matrix = [[0] * column for _ in range(row)]
    wall_nums = int(input())
    for i in range(wall_nums):
        i, j = map(int, input().split())
        matrix[i][j] = -1

    # 只能向上或者向右走
    directions = [(0, 1), (1, 0)]
    # 遍历矩阵来判断
    visited = [[False] * column for _ in range(row)]
    q = deque()
    # 加入起点的位置
    q.append((0, 0))

    while q:
        flag = False
        path = deque()
        dead_path = deque()
        path.append((0, 0))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < column and not visited[nx][ny]:
                    if matrix[nx][ny] == -1 and (nx + 1 > row -1 or ny + 1 > column-1):
                        print(f"********{nx} {ny}")
                        # q.append((nx, ny))
                        dead_path = path.copy()
                        break
                    if matrix[nx][ny] == -1:  # 碰到墙了
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    # fixme: 这里有问题，应该只加入能顺利到出口的点加入队列
                    path.append((nx, ny))
                    if nx >= row - 1 and ny >= column - 1:
                        flag = True
                        # deadlock = False
                        break
                #     matrix[nx][ny] = 1
        for p1, q1 in path:
            # print(f"flag is {flag}")
            # 判断是否可以到达，可以到达的话，把经过的点置为1
            if flag:
                matrix[p1][q1] = 1
        print(f"dead path is {dead_path}")
        for p2, q2 in dead_path:
            if matrix[p2][q2] != 1:
                print("here*********")
                matrix[p2][q2] = 2
    # 统计matrix中1和2的个数
    print("This is matrix &&&&&&")
    print(matrix)
    trap_count, unreachable = 0, 0
    for item in matrix:
        for row in item:
            if row == 2:
                trap_count += 1
            elif row == 0:
                unreachable += 1
            # if matrix[nx][ny] == -1:  # 碰到墙了
            #     continue
    print(trap_count, unreachable)


if __name__ == '__main__':
    bfs()