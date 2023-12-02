"""
描述
给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩都按先录入排列在前的规则处理。

例示：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩
peter     96
jack      70
Tom       70
smith     67

从低到高
smith     67
jack      70
Tom       70
peter     96
注：0代表从高到低，1代表从低到高

数据范围：人数：1≤n≤200

进阶：时间复杂度：O(nlogn) ，空间复杂度：O(n)
输入描述：
第一行输入要排序的人的个数n，第二行输入一个整数表示排序的方式，之后n行分别输入他们的名字和成绩，以一个空格隔开

输出描述：
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开

示例1：
3
0
fang 90
yang 50
ning 70

输出：
fang 90
ning 70
yang 50

#示例2
输入：
3
1
fang 90
yang 50
ning 70

输出：
yang 50
ning 70
fang 90
"""

from typing import List

a = int(input())
b = int(input())

def insert_into_sorted_list(num_list:List, new_num:int,sorting:int)->int:
    for i, num in enumerate(num_list):
        if (sorting == 1 and new_num < num) or (sorting == 0 and new_num > num):
            pos = i
            break
    else:
        # 如果新数字应该是列表中最大的数字，则将其添加到列表的末尾
        num_list.append(new_num)
        pos = len(num_list) - 1
    return pos

empty_list = []
sorted_list = []
raw_list = []
for i in range(a):
    row = input().split(' ')
    if not empty_list:
        empty_list.append(row)
    elif sorted_list and  b == 1 and int(row[1]) < sorted_list[-1]:
        pos = insert_into_sorted_list(sorted_list, int(row[1]), b)
        empty_list.insert(pos, row)
    elif sorted_list and  b == 0 and int(row[1]) > sorted_list[-1]:
        pos =insert_into_sorted_list(sorted_list, int(row[1]), b)
        #  sorted_list.index(int(row[1]))
        empty_list.insert(pos, row)
    else:
        empty_list.append(row)
    raw_list.append(int(row[1]))
    if b == 1:
        sorted_list = sorted(raw_list)
    elif b == 0:
        sorted_list = sorted(raw_list, reverse=True)
for item in empty_list:
    print(item[0], item[1])

