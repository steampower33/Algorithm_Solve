def solution(N, stages):
    l = len(stages)
    failure = dict()
    last_cnt = 0
    a = list()

    for _ in range(1, N+1):
        if (l - last_cnt) != 0:
            failure[_] = stages.count(_) / (l - last_cnt)
        elif (l - last_cnt) == 0:
            failure[_] = 0
        l -= last_cnt
        last_cnt = stages.count(_)

    for _ in failure.items(): a.append(_)

    a.sort(key=lambda x: x[1], reverse=True)

    return [_[0] for _ in a]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))