def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    s = list()

    for _ in lost:
        if _ in reserve:
            reserve.remove(_)
            s.append(_)

    for _ in s:
        if _ in lost:
            lost.remove(_)

    answer = n - len(lost)

    for _ in lost:
        if _ - 1 in reserve:
            answer += 1
            reserve.remove(_ - 1)
            continue
        if _ + 1 in reserve:
            answer += 1
            reserve.remove(_ + 1)
            continue

    return answer