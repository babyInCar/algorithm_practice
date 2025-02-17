"""
一个荒岛上有若干人，岛上只有一条路通往岛屿两端的港口，大家需要逃往两端的港口才可逃生。

假定每个人移动的速度一样，且只可选择向左或向右逃生。

若两个人相遇，则进行决斗，战斗力强的能够活下来，并损失掉与对方相同的战斗力；若战斗力相同，则两人同归于尽。

输入描述
给定一行非 0 整数数组，元素个数不超过30000；

正负表示逃生方向（正表示向右逃生，负表示向左逃生），绝对值表示战斗力，越左边的数字表示里左边港口越近，逃生方向相同的人永远不会发生决斗。

输出描述
能够逃生的人总数，没有人逃生输出0，输入异常时输出-1。

用例：
5 10 8 -8 -5

输出：
2
"""

from collections import deque


def get_last_nums(people):
    """获取最后生存的人数"""
    len1 = len(people)
    stack = []
    if not people or not isinstance(people, list) or len(people) > 30000:
        return -1

    for item in people:
        # 进栈
        if item == 0:
            return -1  # 输入异常，不具备战斗力
        if item > 0:
            stack.append(item)
        else:
            while stack and stack[-1] > 0:
                # 与栈顶的元素格斗
                temp = stack[-1]
                if temp == abs(item):
                    stack.pop()
                    break
                elif temp + item > 0:
                    stack[-1] = stack[-1] + item
                    break
                else:
                    stack.pop()
                    item += temp
        print(f"stack is: {stack}")
    return len(stack)


if __name__ == '__main__':
    l1 = [5, -3, 4, -2, 8, -7]
    print(f"最后留下的人数为：{get_last_nums(l1)}")