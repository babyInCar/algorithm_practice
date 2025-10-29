from functools import lru_cache


def count_valid_sequences(n):
    init_parity = 0 if n % 2 == 0 else 1  # 0: 偶数, 1: 奇数

    # 记忆化递归：仅保留必要状态，不存储完整数列
    # current_num: 当前数列的最后一个数
    # prev_parity: 最后一个数的奇偶性（0偶1奇）
    # mode: 模式（0全偶/1全奇/2相间）
    # min_len: 数列最小长度要求（1或2）
    @lru_cache(maxsize=None)
    def dp(current_num, prev_parity, mode, min_len):
        count = 1 if min_len <= 1 else 0  # 长度≥min_len时，自身算1个

        max_next = current_num // 2
        if max_next == 0:
            return count

        for next_num in range(1, max_next + 1):
            next_parity = 0 if next_num % 2 == 0 else 1
            valid = False

            if mode == 0:  # 全偶：下一个必须是偶数
                valid = (next_parity == 0)
            elif mode == 1:  # 全奇：下一个必须是奇数
                valid = (next_parity == 1)
            elif mode == 2:  # 相间：下一个与前一个奇偶不同
                valid = (next_parity != prev_parity)

            if valid:
                # 递归计算：下一个数作为新的current_num，min_len降为1（后续长度只需≥1即可）
                count += dp(next_num, next_parity, mode, 1)

        return count

    total = 0
    # 模式0：全偶（仅初始为偶时有效，min_len=1包含自身）
    if init_parity == 0:
        total += dp(n, init_parity, 0, 1)
    # 模式1：全奇（仅初始为奇时有效，min_len=1包含自身）
    if init_parity == 1:
        total += dp(n, init_parity, 1, 1)
    # 模式2：相间（min_len=2，自身不算，仅统计长度≥2的数列）
    total += dp(n, init_parity, 2, 2)

    return total


if __name__ == '__main__':
    n = int(input())
    print(count_valid_sequences(n))