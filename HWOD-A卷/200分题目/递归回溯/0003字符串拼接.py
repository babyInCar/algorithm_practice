"""
给定 M（0 < M ≤ 30）个字符（a-z），从中取出任意字符（每个字符只能用一次）拼接成长度为 N（0 < N ≤ 5）的字符串，
要求相同的字符不能相邻，计算出给定的字符列表能拼接出多少种满足条件的字符串，
输入非法或者无法拼接出满足条件的字符串则返回0。

输入描述
给定的字符列表和结果字符串长度，中间使用空格(" ")拼接

输出描述
满足条件的字符串个数

用例1
输入
aab 2
输出
2
说明
只能构成ab,ba。

用例2
输入

abc 2
输出
6
说明
可以构成：ab ac ba bc ca cb 。
"""


def generate_combinations(input_str, target_length, current, results, used):

    if len(current) == int(target_length):
        results.add(current)
        return

    for i in range(len(input_str)):
        # 跳过已使用或者连续重复的字符串
        if used[i] or (current and current[-1] == input_str[i]):
            continue
        used[i] = True
        generate_combinations(input_str, target_length, current + input_str[i], results, used)
        used[i] = False


def count_unique_combinations(input_str, target_length):
    unique_combinations = set()
    used = [False] * len(input_str)
    generate_combinations(input_str, target_length, "", unique_combinations, used)
    return len(unique_combinations)


if __name__ == '__main__':
    input_str, n = input().split(" ")
    print(count_unique_combinations(input_str, n))




