def solution(n):
    answer = 0

    third = []

    while True:
        rest = n % 3
        n = n // 3
        third.append(rest)
        if n == 1 or n == 2:
            third.append(n)
            break
        if n == 0:
            break

    for _ in range(len(third)):
        answer += third[-_ - 1] * 3 ** _

    return answer