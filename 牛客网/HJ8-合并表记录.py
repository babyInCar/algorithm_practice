"""
难度：入门级
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1：
输入：4
0 1
0 2
1 2
3 4
输出：0 3
1 2
3 4

示例2：
输入:3
0 1
0 2
8 9

输出：
0 3
8 9
"""
n = int(input())
dc = {}

for i in range(n):
    row = input().split()
    if row[0] in dc.keys():
        dc[row[0]] += int(row[1])
    else:
        dc[row[0]] = int(row[1])

sorted_list = sorted(dc.items(), key=lambda x: int(x[0]))

sorted_dict = {}
for item in sorted_list:
    sorted_dict[item[0]] = item[1]
for key, value in sorted_dict.items():
    print(key, value)