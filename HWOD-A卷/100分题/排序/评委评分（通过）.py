def main():
    data = input().split(',')
    if len(data) != 2:
        print(-1)
        return
    try:
        M = int(data[0])
        N = int(data[1])
    except:
        print(-1)
        return

    # 检查M和N范围
    if not (3 <= M <= 10) or not (3 <= N <= 100):
        print(-1)
        return

    scores = []
    for i in range(M):
        line = input().split(',')
        if len(line) != N:
            print(-1)
            return
        try:
            row = list(map(int, line))
        except:
            print(-1)
            return
        for score in row:
            if not (1 <= score <= 10):
                print(-1)
                return
        scores.append(row)

    # 转置scores，得到每个选手的分数
    player_scores = list(zip(*scores))   # 每个元素是一个元组，表示一个选手的分数列表

    # 为每个选手计算总分和频率列表
    players = []
    for idx, scores_list in enumerate(player_scores, start=1):
        total = sum(scores_list)
        freq = [0] * 10   # freq[0] for 10, freq[1] for 9, ... freq[9] for 1
        for s in scores_list:
            if s == 10:
                freq[0] += 1
            elif s == 9:
                freq[1] += 1
            elif s == 8:
                freq[2] += 1
            elif s == 7:
                freq[3] += 1
            elif s == 6:
                freq[4] += 1
            elif s == 5:
                freq[5] += 1
            elif s == 4:
                freq[6] += 1
            elif s == 3:
                freq[7] += 1
            elif s == 2:
                freq[8] += 1
            elif s == 1:
                freq[9] += 1
        players.append((total, freq, idx))

    # 排序：按总分降序，然后按频率列表降序（通过取负实现）
    sorted_players = sorted(players, key=lambda x: (-x[0], tuple(-c for c in x[1])))
    # 取前3名编号
    top3 = [player[2] for player in sorted_players[:3]]
    # 输出为逗号分隔的字符串
    print(','.join(map(str, top3)))


if __name__ == '__main__':
    main()