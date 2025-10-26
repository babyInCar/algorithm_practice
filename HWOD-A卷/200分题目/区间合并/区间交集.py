"""
给定一组闭区间，其中部分区间存在交集。

任意两个给定区间的交集，称为公共区间(如:[1,2],[2,3]的公共区间为[2,2]，[3,5],[3,6]的公共区间为[3,5])。

公共区间之间若存在交集，则需要合并(如:[1,3],[3,5]区间存在交集[3,3]，需合并为[1,5])。

按升序排列输出合并后的区间列表。

输入描述
一组区间列表，

区间数为 N: 0<=N<=1000;

区间元素为 X: -10000<=X<=10000。

备注
区间元素均为数字，不考虑字母、符号等异常输入。
单个区间认定为无公共区间。
输出描述
升序排列的合并区间列表

输入：
4
0 3
1 3
3 5
3 6

输出：
1 5
"""


def main():
    a = int(input())
    sorted_intervals = []
    for i in range(a):
        sorted_intervals.append(list(map(int, input().split())))

    sorted_intervals = sorted(sorted_intervals, key=lambda x:x[0])
    merged = [sorted_intervals[0]]

    for sorted in sorted_intervals:
        pass




if __name__ == '__main__':
    main()