import random


def generate_maze(width, height):
    # 初始化迷宫，所有墙都存在（使用位掩码表示四个方向的墙）
    maze = [[0b1111 for _ in range(height)] for _ in range(width)]
    visited = [[False for _ in range(height)] for _ in range(width)]
    stack = [(0, 0)]
    visited[0][0] = True

    # 方向映射：方向名、(dx, dy)、当前墙掩码、相反方向墙掩码
    directions = [
        ('N', (0, -1), 0b0001, 0b0010),
        ('S', (0, 1), 0b0010, 0b0001),
        ('E', (1, 0), 0b0100, 0b1000),
        ('W', (-1, 0), 0b1000, 0b0100)
    ]

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dir_name, (dx, dy), current_wall, opposite_wall in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[nx][ny]:
                neighbors.append((nx, ny, current_wall, opposite_wall))

        if neighbors:
            nx, ny, current_wall, opposite_wall = random.choice(neighbors)
            # 拆除当前单元格和邻居的墙
            maze[x][y] &= ~current_wall
            maze[nx][ny] &= ~opposite_wall
            visited[nx][ny] = True
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze


def print_maze(maze):
    width = len(maze)
    height = len(maze[0]) if width > 0 else 0
    # 打印顶部边界
    print(" " + "_" * (width * 2 - 1))
    for y in range(height):
        # 构建当前行的顶部和右侧墙
        top = ["|"]
        for x in range(width):
            cell = maze[x][y]
            # 检查南墙是否存在（当前单元格的南墙是下方单元格的北墙）
            south_wall = cell & 0b0010
            # 检查东墙是否存在
            east_wall = cell & 0b0100
            # 绘制南墙（用"_"表示）或空格
            top.append("_" if south_wall else " ")
            # 绘制东墙（用"|"表示）或空格
            top.append("|" if east_wall else " ")
        print("".join(top))


if __name__ == "__main__":
    maze = generate_maze(10, 10)
    print_maze(maze)
