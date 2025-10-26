"""
总共有 n 个人在机房，每个人有一个标号（1<=标号<=n），他们分成了多个团队，需要你根据收到的 m 条消息判定指定的两个人是否在一个团队中，具体的：

消息构成为 a b c，整数 a、b 分别代表两个人的标号，整数 c 代表指令
c == 0 代表 a 和 b 在一个团队内
c == 1 代表需要判定 a 和 b 的关系，如果 a 和 b 是一个团队，输出一行’we are a team’,如果不是，输出一行’we are not a team’
c 为其他值，或当前行 a 或 b 超出 1~n 的范围，输出‘da pian zi’
输入描述
第一行包含两个整数 n，m(1<=n,m<100000),分别表示有 n 个人和 m 条消息
随后的 m 行，每行一条消息，消息格式为：a b c(1<=a,b<=n,0<=c<=1)
输出描述
c ==1,根据 a 和 b 是否在一个团队中输出一行字符串，在一个团队中输出‘we are a team‘,不在一个团队中输出’we are not a team’
c 为其他值，或当前行 a 或 b 的标号小于 1 或者大于 n 时，输出字符串‘da pian zi‘
如果第一行 n 和 m 的值超出约定的范围时，输出字符串”Null“。

5 7
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1

输出
we are a team
we are a team
we are a team
we are not a team
"""

import sys


class UnionFind:
    def __init__(self, size):
        # 初始化父节点：每个节点的父节点是自己（1-based索引）
        self.parent = list(range(size + 1))  # 索引0 unused
        # 秩：用于按秩合并，初始化为1
        self.rank = [1] * (size + 1)

    def find(self, x):
        """查找x的根节点，同时路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 递归压缩路径
        return self.parent[x]

    def union(self, x, y):
        """合并x和y所在的集合，按秩合并"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return  # 已在同一集合，无需合并
        # 秩小的树合并到秩大的树的根节点下
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1


def main():
    # 读取第一行n和m
    first_line = sys.stdin.readline().strip()
    if not first_line:
        print("Null")
        return
    try:
        n, m = map(int, first_line.split())
    except ValueError:
        print("Null")
        return

    # 校验n和m的范围（1<=n,m <100000）
    if not (1 <= n < 100000 and 1 <= m < 100000):
        print("Null")
        return

    # 初始化并查集
    uf = UnionFind(n)

    # 处理m条消息
    for _ in range(m):
        line = sys.stdin.readline().strip()
        if not line:
            print("da pian zi")
            continue
        try:
            a, b, c = map(int, line.split())
        except ValueError:
            print("da pian zi")
            continue

        # 校验a和b的范围（1<=a,b <=n）
        if a < 1 or a > n or b < 1 or b > n:
            print("da pian zi")
            continue

        # 处理指令c
        if c == 0:
            # 合并a和b所在的团队
            uf.union(a, b)
        elif c == 1:
            # 查询a和b是否在同一团队
            if uf.find(a) == uf.find(b):
                print("we are a team")
            else:
                print("we are not a team")
        else:
            # c为其他值
            print("da pian zi")


if __name__ == "__main__":
    main()


# def main():
#     people, message = map(int, input().split())
#     if people > 100000 or message > 100000:
#         print("Null")
#         return
#
#     message_list = [list(map(int, input().split())) for _ in range(message)]
#     message_list = sorted(message_list, key=lambda x: x[-1])
#
#     team_list = []  # set() for _ in range(people)
#     for message in message_list:
#         if (message[0] < 1 or message[0] > people) or (message[1] < 1 or message[1] > people):
#             print("da pian zi")
#             break
#         if message[-1] == 0:
#             if not team_list:
#                 team_list.append(set([message[0], message[1]]))
#             else:
#                 for team in team_list:
#                     if message[0] in team or message[1] in team:
#                         team.add(message[0])
#                         team.add(message[1])
#                         break
#                     else:
#                         team_list.append(set([message[0], message[1]]))
#         elif message[-1] == 1:
#             for index, item in enumerate(team_list):
#                 if message[0] in item and message[1] in item:
#                     print("we are a team")
#                     break
#                 # if index == len(team_list):
#             else:
#                 print("we are not a team")
#         else:
#             print("da pian zi")
#
#
# if __name__ == '__main__':
#     main()