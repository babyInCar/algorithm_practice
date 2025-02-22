"""

周末爬山

"""
from collections import deque


def climb_mountain(m, n, k, mountain):
    # 定义四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 初始化访问数组和队列
    visited = [[False] * n for _ in range(m)]
    queue = deque([(0, 0, 0)])  # (x, y, steps)
    visited[0][0] = True

    max_height = mountain[0][0]
    min_steps = 0

    while queue:
        x, y, steps = queue.popleft()
        print(f"x,y,steps === {x}, {y}, {steps}")
        # 检查是否需要更新最大高度和最短步数
        if mountain[x][y] > max_height or (mountain[x][y] == max_height and steps < min_steps):
            max_height = mountain[x][y]
            min_steps = steps
        print(f"max height is {max_height}")

        # 检查四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # print(f"===nx=={nx}")
            # print(f"===ny=={ny}")
            # 检查新位置是否在地图范围内且未被访问过
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                # 检查高度差是否在允许范围内
                if abs(mountain[nx][ny] - mountain[x][y]) <= k:
                    queue.append((nx, ny, steps + 1))
                    visited[nx][ny] = True

    # 如果没有爬到更高的山峰，返回0 0
    return (max_height, min_steps) if max_height > mountain[0][0] else (0, 0)


# 读取输入
m, n, k = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(m)]

# 计算结果并输出
height, steps = climb_mountain(m, n, k, mountain)
print(f"{height} {steps}")
