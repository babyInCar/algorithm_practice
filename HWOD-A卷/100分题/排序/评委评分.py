

def judge(score_list, row_count, judge_count):
    if not (3 <= row_count <= 100) or not (3 <= judge_count <= 10):
        return -1

    each_list = [list(row) for row in zip(*score_list)]
    indexed_data = []
    for idx, sublist in enumerate(each_list, start=1):
        total = sum(sublist)
        freq = [0] * 10
        for s in sublist:
            freq[10-s] += 1
        indexed_data.append((total, freq, idx))
    sorted_data = sorted(indexed_data, key=lambda x: (-x[0], tuple(-c for c in x[1])))
    ret_list = [item[2] for item in sorted_data[:3]]
    return ','.join(map(str, ret_list))


if __name__ == '__main__':
    j, a = map(int, input().split(','))
    score_list = []

    for i in range(j):
        l1= list(map(int, input().split(",")))
        score_list.append(l1)
    print(judge(score_list, a, j))

    # [[10, 6, 9, 7, 6],
    # [9, 10, 6, 7, 5],
    # [8, 10, 6, 5, 10],
    # [9, 10, 8, 4, 9]]