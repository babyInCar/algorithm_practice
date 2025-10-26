"""
某部门开展 Family Day 开放日活动，其中有个从桶里取球的游戏，游戏规则如下：有 N 个容量一样的小桶等距排开，且每个小桶都默认装了数量不等的小球，
每个小桶装的小球数量记录在数组 bucketBallNums 中，游戏开始时，要求所有桶的小球总数不能超过 SUM，如果小球总数超过 SUM，则需对所有的小桶统一
设置一个容量最大值 maxCapacity，并需将超过容量最大值的小球拿出来，直至小桶里的小球数量小于 maxCapacity。请您根据输入的数据，计算从每个小桶
里拿出的小球数量？
限制规则一：所有小桶的小球总和小于 SUM，则无需设置容量值 maxCapacity，并且无需从小桶中拿球出来，返回结果[]
限制规则二：如果所有小桶的小球总和大于 SUM，则需设置容量最大值 maxCapacity，并且需从小桶中拿球出来，返回从每个小桶拿出的小球数量组成的数组

输入描述
第一行输入 2 个正整数，数字之间使用空格隔开，其中：第一个数字表示 SUM 第二个数字表示 bucketBallNums 数组长度.
第二行输入 N 个正整数，数字之间使用空格隔开，表示 bucketBallNums 的每一项
备注
1 ≤ bucketBallNums[i] ≤ 10^9 1 ≤ bucketBallNums.length = N ≤ 10^5 1 ≤ maxCapacity ≤ 10^9 1 ≤ SUM ≤ 10^9

输出描述
从每个小桶里拿出的小球数量，并使用一维数组表示

输入
14 7
2 3 2 5 5 1 4

输出
[0,1,0,3,3,0,2]

问题的核心在于判断：
1. 是否超出了容量限制
2. 如果超出了容量限制，需要确定maxCapacity, 通过二分法来确定 left = 0,right=maxBall,每次枚举mid=(left+right)/2作为本次maxCapacity的尝试值，边界移动规律：
    check(mid) == true, 移动左边界，更新left=mid
    check(mid) == false, 移动右边界，更新right=mid-1
3.check(mid)的逻辑：每个桶在容量限制下能够放置的小球数量变为min(mid,bucket[i]),累加容量限制下小球的数量，判断是否小于等于SUM,如果小于等于SUM,则返回true，否则返回False
4.二分结束条件为 left == right结束，maxCapacity就是left，每个桶移除的小球数量就为max(0, bucket[i] - maxCapacity),按题目要求输出答案即可
"""


def check(mid, ball_nums, total_cap):
    """判断是否超出容量限制"""
    if sum([min(mid, ball_num) for ball_num in ball_nums]) <= int(total_cap):
        return True
    else:
        return False


def main():
    total_cap, we = input().split()
    each_ball_nums = list(map(int, input().split()))

    if sum(each_ball_nums) <= int(total_cap):
        print("[]")
        return

    left, right = 0, max(each_ball_nums)
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, each_ball_nums, total_cap):
            left = mid
        else:
            right = mid - 1

    remove_ball_nums = []
    for bucket in each_ball_nums:
        remove_ball_nums.append(max(0, bucket - left))
    print("[" + ",".join(str(max(0, x - left)) for x in each_ball_nums) + "]")
    # print(remove_ball_nums)


if __name__ == '__main__':
    main()

