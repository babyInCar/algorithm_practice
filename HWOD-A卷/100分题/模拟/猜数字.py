"""

"""


def main():
    n = int(input())
    ans = [input().split() for _ in range(n)]

    match_count = 0
    result = ""

    # 预编译验证函数，避免重复计算
    def check_match(candidate):
        candidate_str = f"{candidate:04d}"
        for guess, expected in ans:
            countA, countB = 0, 0
            # 使用数组记录数字出现次数，比字典更快
            count_candidate = [0] * 10
            count_guess = [0] * 10

            # 先计算A（位置和数字都正确）
            for i in range(4):
                c1 = int(candidate_str[i])
                c2 = int(guess[i])
                if c1 == c2:
                    countA += 1
                else:
                    count_candidate[c1] += 1
                    count_guess[c2] += 1

            # 再计算B（数字正确但位置不对）
            countB = sum(min(count_candidate[i], count_guess[i]) for i in range(10))

            if f"{countA}A{countB}B" != expected:
                return False
        return True

    # 遍历所有可能的四位数
    for i in range(10000):
        if check_match(i):
            match_count += 1
            result = f"{i:04d}"
            # 如果找到第二个匹配，立即返回
            if match_count > 1:
                print("NA")
                return

    print(result if match_count == 1 else "NA")


if __name__ == "__main__":
    main()