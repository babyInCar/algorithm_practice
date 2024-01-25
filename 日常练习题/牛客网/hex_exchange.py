"""
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在
1≤n≤231−1
1≤n≤231−1
输入描述：
输入一个十六进制的数值字符串。
输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
"""

import sys

num_hex = input()
hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
result = 0
n = 0

for item in num_hex[-1:1:-1]:
    try:
        result += int(item) * pow(16, n)
    except:
        result += int(hex_map.get(item)) * pow(16, n)
    n += 1

print(result)