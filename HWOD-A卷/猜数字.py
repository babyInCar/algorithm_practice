def calculate_xy(secret, guess):
    """计算猜测guess相对于谜底secret的XAYB，返回(X, Y)"""
    # 计算A：位置和数字都正确的数量
    a = sum(s == g for s, g in zip(secret, guess))

    # 计算每个数字的出现次数（用于B的计算）
    from collections import defaultdict
    secret_counts = defaultdict(int)
    guess_counts = defaultdict(int)

    for s, g in zip(secret, guess):
        if s != g:  # 排除已计入A的数字
            secret_counts[s] += 1
            guess_counts[g] += 1

    # 计算B：数字正确但位置错误的数量（取每个数字出现次数的最小值之和）
    b = 0
    for num in guess_counts:
        b += min(guess_counts[num], secret_counts.get(num, 0))

    return (a, b)


def find_secret():
    n = int(input())
    if n <= 0 or n >= 100:
        print("NA")
        return

    # 读取所有猜测和提示，存储为(guess_str, x, y)
    clues = []
    for _ in range(n):
        parts = input().strip().split()
        if len(parts) != 2:
            print("NA")
            return
        guess_str, hint = parts
        # 验证猜测是4位数字
        if len(guess_str) != 4 or not guess_str.isdigit():
            print("NA")
            return
        # 解析提示（如"1A1B" -> x=1, y=1）
        if 'A' not in hint or 'B' not in hint:
            print("NA")
            return
        a_part, b_part = hint.split('A')
        if len(b_part) == 0 or b_part[-1] != 'B':
            print("NA")
            return
        try:
            x = int(a_part)
            y = int(b_part[:-1])
        except ValueError:
            print("NA")
            return
        # 验证X和Y的合法性（X+Y <=4，且均为非负整数）
        if x < 0 or y < 0 or (x + y) > 4:
            print("NA")
            return
        clues.append((guess_str, x, y))

    # 生成所有可能的四位数候选谜底（1000-9999）
    candidates = [str(num).zfill(4) for num in range(1000, 10000)]

    # 筛选符合所有提示的候选谜底
    valid_secrets = []
    for secret in candidates:
        valid = True
        for (guess, x, y) in clues:
            calc_x, calc_y = calculate_xy(secret, guess)
            if calc_x != x or calc_y != y:
                valid = False
                break
        if valid:
            valid_secrets.append(secret)

    # 确定结果
    if len(valid_secrets) == 1:
        print(valid_secrets[0])
    else:
        print("NA")


if __name__ == "__main__":
    find_secret()