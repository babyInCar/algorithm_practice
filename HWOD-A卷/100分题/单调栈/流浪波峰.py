import sys

# 找到左边小于本身高度的最近点
def find_left_small(nums):
    n = len(nums)
    left = [-1] * n
    # 单调栈 维持一个单调递增
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    return left


# 找到右边小于本身高度的最近点
def find_right_smaller(nums):
    n = len(nums)
    right = [-1] * n
    # 单调栈 维持单调递增
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

def main():
    line = sys.stdin.readline().strip()
    heights = list(map(int, line.split()))
    n = len(heights)

    # 数量小于三肯定不存在指定元组
    if n < 3:
        print(-1)
        return

    left = find_left_small(heights)
    # print(f"left is {left}")
    right = find_right_smaller(heights)
    # print(f"right is {right}")

    res = float("inf")
    for j in range(n):
        # 左侧小于自己最近的点
        i = left[j]
        k = right[j]
        # 左侧或右侧不存在这样的点
        if i == -1 or k == -1:
            continue
        res = min(res, k - i)

    # 输出结果
    print(-1 if res == float("inf") else res)


if __name__ == "__main__":
    main()

