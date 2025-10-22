
# 代码分析题
def func(a, b=[]):
    b.append(a)
    return b

import time

def wrapper(func):
    def inner(a, b=[]):
        start = time.time()
        func()
        end = time.time()
        cost = end - start
        print("time cost is:", cost)
    return inner


@wrapper
def func_test():
    time.sleep(3)


if __name__ == '__main__':
    print(func(1))  # 输出什么？
    # print(b)
    print(func(2))  # 输出什么？为什么？

    func_test(1, [])