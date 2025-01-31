"""
一只贪吃的猴子，来到一个果园，发现许多串香蕉排成一行，每串香蕉上有若干根香蕉。每串香蕉的根数由数组numbers给出。猴子获取香蕉，
每次都只能从行的开头或者末尾获取，并且只能获取N次，求猴子最多能获取多少根香蕉。

输入描述
第一行为数组numbers的长度
第二行为数组numbers的值每个数字通过空格分开
第三行输入为N，表示获取的次数

输出描述
按照题目要求能获取的最大数值

示例1
输入：
7
1 2 2 7 3 6 1
3
输出
10

示例2
输入
3
1 2 3
3
输出
6

说明
全部获取所有的香蕉，因此最终根数为1+2+3 = 6

"""
from typing import List

class Solution:
    def LBS(self)->int:

        a = int(input())
        number_list = input().split(" ")
        c = int(input())

        head = 0
        tail = len(number_list) - 1
        move_nums = 0
        total = 0
        while head <= tail and move_nums < c:
            if number_list[head] > number_list[tail]:
                total += int(number_list[head])
                head += 1
                move_nums += 1
            else:
                total += int(number_list[tail])
                tail -= 1
                move_nums += 1
        return total


s = Solution()
print(s.LBS())