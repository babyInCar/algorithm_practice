"""
在一条笔直的公路上安装了N个路灯，从位置0开始安装，路灯之间间距固定为100米。 每个路灯都有自己的照明半径，请计算第一个路灯和最后一个路灯之间，无法照明的区间的长度和。

输入描述
第一行为一个数N，表示路灯个数，1<=N<=100000 第二行为N个空格分隔的数，表示路灯的照明半径，1<=照明半径<=100000*100

输出描述
第一个路灯和最后一个路灯之间，无法照明的区间的长度和.

输入：
2
50 50

输出：
0

输入：
4
50 70 20 70

输出：
20
"""


def main():
    """通过区间来判断"""
    a = int(input())
    radius_list = list(map(int, input().split()))

    if a == 1:
        print(0)
        return

    point_list = []
    for index, radius in enumerate(radius_list):
        start = index * 100 - radius
        end = index * 100 + radius
        point_list.append((start, end))

    sorted_intervals = sorted(point_list, key=lambda x: x[0])
    # print(sorted_intervals)
    merged = [list(sorted_intervals[0])]
    # 这一段是区间合并的代码
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # 重叠或相邻，合并为更大的区间
            last[1] = max(last[1], current[1])
        else:
            merged.append(list(current))

    covered = 0
    target_start = 0
    target_end = (a - 1) * 100
    for (s, e) in merged:
        overlap_s = max(s, target_start)
        overlap_e = min(e, target_end)
        if overlap_s < overlap_e:
            covered += overlap_e - overlap_s

    # 计算无法照明的距离
    total_length = target_end - target_start
    unit = total_length - covered

    # for index, item in enumerate(point_list):
    #     if index < len(point_list) - 1 and point_list[index+1][0] > point_list[index][1]:
    #         # print(f"====={point_list[index+1][0] - point_list[index][1]}")
    #         diff_distance += point_list[index+1][0] - point_list[index][1]
    print(unit)


if __name__ == '__main__':
    main()
