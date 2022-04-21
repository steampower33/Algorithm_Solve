
def solution(absolutes, signs):
    answer = absolutes[0]

    for _ in range(1, len(absolutes)):
        if signs[_] == 'true':
            answer += absolutes[_]
        else:
            answer -= absolutes[_]

    return answer