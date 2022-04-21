def solution(numbers):
    answer = 0

    nums = dict()

    for _ in range(0, 10):
        nums[_] = 0

    for _ in numbers:
        nums[_] += 1

    for _ in nums.items():
        if _[1] == 0:
            answer += _[0]

    return answer

print(solution([1,2,3,4,6,7,8,0]))