"""
流浪地球计划在赤道上均匀部署了 N 个转向发动机，按位置顺序编号为 0 ~ N

初始状态下所有的发动机都是未启动状态
发动机启动的方式分为“手动启动”和“关联启动”两种方式
如果在时刻 1 一个发动机被启动，下一个时刻 2 与之相邻的两个发动机就会被“关联启动”
如果准备启动某个发动机时，它已经被启动了，则什么都不用做
发动机 0 与发动机 N-1 是相邻的
地球联合政府准备挑选某些发动机在某些时刻进行“手动启动”。当然最终所有的发动机都会被启动。哪些发动机最晚被启动呢？

输入描述
第一行两个数字 N 和 E，中间有空格

N 代表部署发动机的总个数，1 < N ≤ 1000
E 代表计划手动启动的发动机总个数，1 ≤ E ≤ 1000，E ≤ N
接下来共 E 行，每行都是两个数字 T 和 P，中间有空格

T 代表发动机的手动启动时刻，0 ≤ T ≤ N
P 代表次发动机的位置编号，0 ≤ P < N
输出描述
第一行一个数字 N， 以回车结束

N 代表最后被启动的发动机个数
第二行 N 个数字，中间有空格，以回车结束

每个数字代表发动机的位置编号，从小到大排序

输入：
8 2
0 2
0 6

输出
2
0 4

8个发动机；
时刻0启动（2,6）;
时刻1启动（1,3,5,7）（其中1,3被2关联启动，5,7被6关联启动）；
时刻2启动（0,4）（其中0被1,7关联启动，4被3,5关联启动）；
至此所有发动机都被启动，最后被启动的有2个，分别是0和4。
"""

import sys
from collections import deque


def get_neighbors(x, N):
    """获取环形数组中节点 x 的邻居"""
    if x == 0:
        return [N - 1, 1]
    elif x == N - 1:
        return [N - 2, 0]
    return [x - 1, x + 1]


def main():
    N, E = map(int, sys.stdin.readline().split())
    # 哈希表，用于存储每个启动时刻启动的发动机列表
    table = {}
    min_key = float('inf')
    # 遍历每条启动信息
    for _ in range(E):
        T, P = map(int, sys.stdin.readline().split())
        if T not in table:
            table[T] = []
        # 将发动机编号添加到相应的启动时刻中
        table[T].append(P)
        min_key = min(min_key, T)

    queue = deque()
    # 用于标记发动机是否已经启动
    check_list = [False] * N
    # 已经启动的数量
    total = 0
    cur_time = min_key
    last_started = []

    # BFS
    while total < N:
        # 如果当前时刻有发动机要启动
        if cur_time in table:
            for x in table[cur_time]:
                if not check_list[x]:
                    check_list[x] = True
                    queue.append(x)

        q_size = len(queue)
        total += q_size
        # 全部启动完毕
        if total == N:
            last_started.extend(queue)
            break
        # 关联启动当前启动的发动机周边的发动机
        for _ in range(q_size):
            x = queue.popleft()
            for nx in get_neighbors(x, N):
                if not check_list[nx]:
                    check_list[nx] = True
                    queue.append(nx)
        # 时间增加
        cur_time += 1

    last_started.sort()
    print(len(last_started))
    print(" ".join(map(str, last_started)))


if __name__ == "__main__":
    main()

