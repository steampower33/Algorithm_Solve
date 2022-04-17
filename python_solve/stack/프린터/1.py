def solution(priorities, location):
    answer = 0

    while True:
        max_num = max(priorities)
        for _ in range(len(priorities)):
            if max_num == priorities[_]:
                answer += 1
                priorities[_] = 0

                if location == _:
                    return answer
                max_num = max(priorities)
if __name__ == "__main__":
    p = [1, 1, 9, 1, 1, 1]
    l = 0

    print(solution(p,l))