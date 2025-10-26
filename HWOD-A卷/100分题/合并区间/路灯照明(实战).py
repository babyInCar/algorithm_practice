


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

    sorted_intervals = sorted(point_list, key = lambda x: x[0])
    merged = [list(sorted_intervals[0])]
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(current[1], last[1])
        else:
            merged.append(list(current))

    target_start = 0
    target_end = (a-1) * 100
    diff_length = 0
    for (s, e) in merged:
        overlap_s = max(target_start, s)
        overlap_e = min(target_end, e)
        diff_length += overlap_e - overlap_s

    total_length = target_end - target_start
    unit = total_length - diff_length
    print(unit)
    # sorted_intervals = sorted(point_list, key=lambda x: x[0])
    # # print(sorted_intervals)
    # merged = [list(sorted_intervals[0])]
    # # 这一段是区间合并的代码
    # for current in sorted_intervals[1:]:
    #     last = merged[-1]
    #     if current[0] <= last[1]:
    #         # 重叠或相邻，合并为更大的区间
    #         last[1] = max(last[1], current[1])
    #     else:
    #         merged.append(list(current))
    # # print(merged)
    #
    # covered = 0
    # target_start = 0
    # target_end = (a - 1) * 100
    # for (s, e) in merged:
    #     overlap_s = max(s, target_start)
    #     overlap_e = min(e, target_end)
    #     if overlap_s < overlap_e:
    #         covered += overlap_e - overlap_s
    #
    # # 计算无法照明的距离
    # total_length = target_end - target_start
    # unit = total_length - covered

    # diff_distance = 0
    # for index, item in enumerate(point_list):
    #     if index < len(point_list) - 1 and point_list[index+1][0] > point_list[index][1]:
    #         # print(f"====={point_list[index+1][0] - point_list[index][1]}")
    #         diff_distance += point_list[index+1][0] - point_list[index][1]

    # print(diff_distance)


if __name__ == '__main__':
    main()