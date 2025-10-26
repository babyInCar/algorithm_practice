"""
Wonderland是小王居住地一家很受欢迎的游乐园。Wonderland目前有4种售票方式，分别为一日票（1天）、三日票（3天）、周票（7天）和月票（30天）。

每种售票方式的价格由一个数组给出，每种票据在票面时限内可以无限制地进行游玩。例如：
小王在第10日买了一张三日票，小王可以在第10日、第11日和第12日进行无限制地游玩。
小王计划在接下来一年多次游玩该游乐园。小王计划地游玩日期将由一个数组给出。
现在，请您根据给出地售票价格数组和小王计划游玩日期数组，返回游玩计划所需要地最低消费。

输入描述
输入为2个数组：

售票价格数组为costs，costs.length = 4，默认顺序为一日票、三日票、周票和月票。
小王计划游玩日期数组为days，1 ≤ days.length ≤ 365，1 ≤ days[i] ≤ 365，默认顺序为升序。
输出描述
完成游玩计划的最低消费。

用例1
5 14 30 100
1 3 5 20 21 200 202 230

输出
40

"""


def main():
    price_list = list(map(int, input().split()))
    days_list = list(map(int, input().split()))

    dp = [0] * (max(days_list) + 1)
    one_day = price_list[0]
    three_day = price_list[1]
    seven_day = price_list[2]
    month_price = price_list[3]

    index = 0
    for i in range(1, max(days_list)+1):
        if i != days_list[index]:
            dp[i] = dp[i-1]
            continue
        buy_one = (dp[i-1] if i-1 > 0 else 0) + one_day
        buy_three = (dp[i-3] if i-3 > 0 else 0) + three_day
        buy_seven = (dp[i-7] if i-7 > 0 else 0) + seven_day
        buy_month = (dp[i-30] if i-30 > 0 else 0) + month_price

        dp[i] = min(buy_one, buy_three, buy_seven, buy_month)
        index += 1
    print(dp[max(days_list)])


if __name__ == '__main__':
    main()