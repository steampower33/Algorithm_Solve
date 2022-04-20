def solution(lottos, win_nums):
    answer = []

    zero = lottos.count(0)
    min_same = len(set(lottos) & set(win_nums))

    answer = [7-max(1, zero+min_same), 7-max(1, min_same)]

    return answer