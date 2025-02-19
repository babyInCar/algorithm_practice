"""

周末爬山

"""

from collections import deque


def climb_mountain(m, n, k, mountain):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False] * n for _ in range(m)]
    queue = deque([(0, 0, 0)])
    visited[0][0] = True

    max_height = mountain[0][0]
    min_steps = 0

    while queue:

        x, y, steps = queue.popleft()

        if mountain[x][y] > max_height or (mountain[x][y] == max_height and steps < min_steps):
            max_height = mountain[x][y]
            min_steps = steps

        for dx,dy in directions:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if abs(mountain[nx][ny]-mountain[x][y]) <= k:  # 注意边界值
                    queue.append((nx, ny, steps + 1))
                    visited[nx][ny] = True

    return (max_height, min_steps) if max_height > mountain[0][0] else (0, 0)