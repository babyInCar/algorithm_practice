
"""
input:
[50,50,2,3],2

output:
1
"""


def main():
    num_str, num = input().split("],")
    k = int(num)
    num_list = list(map(int, num_str[1:].split(',')))
    num_list_copy = num_list.copy()
    # sorted(num_list_copy)
    num_list_copy.sort()
    mid_value = num_list_copy[len(num_list) // 2]
    # print(mid_nums)
    n = len(num_list)

    res = -1
    diff = float('inf')

    left = n - k
    right = n - 1
    sum_val = sum(num_list[left + 1:])

    # 双指针迭代获取最小值
    while left >= 0:
        tmp = num_list[left] - sum_val
        if abs(tmp - mid_value) < diff:
            diff = abs(tmp - mid_value)
            res = left
        sum_val -= num_list[right]
        right -= 1
        sum_val += num_list[left]
        left -= 1

    return res


if __name__ == '__main__':
    print(main())