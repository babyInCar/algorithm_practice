
def find_all_routes():
    # 读取输入
    X, Y = map(int, input().split())  # X：横向(x∈[0,X-1])，Y：纵向(y∈[0,Y-1])
    wall_num = int(input())
    walls = set()
    for _ in range(wall_num):
        x, y = map(int, input().split())
        walls.add((x, y))  # 墙壁坐标集合

    end_x, end_y = X- 1, Y - 1  # 终点坐标
    all_routes = []  # 存储所有有效路线
    directions = [(1, 0), (0, 1)]  # 仅向东、向北

    # 回溯函数：current_path 记录当前路径（坐标列表）
    def backtrack(x, y, current_path):
        # 到达终点，保存路径（复制当前路径，避免后续修改影响）
        if x == end_x and y == end_y:
            all_routes.append(current_path.copy())
            return

        # 尝试两个方向
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            # 边界校验 + 非墙壁 + 未访问（因仅向东/向北，无重复访问，无需visited数组）
            if 0 <= nx < X and 0 <= ny < Y and (nx, ny) not in walls:
                current_path.append((nx, ny))  # 加入当前路径
                backtrack(nx, ny, current_path)  # 递归
                current_path.pop()  # 回溯：移除最后一个坐标

    # 起点校验：若起点不是墙壁则开始回溯
    if (0, 0) not in walls:
        backtrack(0, 0, [(0, 0)])  # 初始路径包含起点

    # 输出所有路线（按格式整理）
    for idx, route in enumerate(all_routes, 1):
        # 格式：(x1,y1) → (x2,y2) → ... → (xn,yn)
        route_str = " → ".join([f"({x},{y})" for x, y in route])
        print(f"路线{idx}：{route_str}")

    # 可选：输出路线总数
    print(f"\n总路线数：{len(all_routes)}")


if __name__ == '__main__':
    find_all_routes()