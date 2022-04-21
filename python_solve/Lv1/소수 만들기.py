from itertools import combinations

def solution(nums):
    answer = 0

    for _ in list(combinations(nums, 3)):
        s = sum(_)
        cnt = 2
        for i in range(2, s):
            if s % i == 0:
                break
            cnt += 1
            if cnt == s:
                answer += 1

    return answer