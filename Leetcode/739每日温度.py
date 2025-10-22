from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    ret_list = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_index = stack.pop()
            ret_list[prev_index] = i - prev_index
        stack.append(i)
    return ret_list


if __name__ == '__main__':
    rs = dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
    print(rs)