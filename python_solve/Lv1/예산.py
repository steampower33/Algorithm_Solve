def solution(d, budget):
    answer = 0

    d.sort()

    m = 0
    for _ in d:
        if m+_ <= budget:
            m += _
            answer += 1
        else:
            break

    return answer