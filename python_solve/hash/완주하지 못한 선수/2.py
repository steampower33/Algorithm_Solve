def solution(participant, completion):
    unfinished = {}

    for _ in range(len(completion)):

        isExist = unfinished.get(completion[_])

        if isExist == None:
            unfinished[completion[_]] = 1
        else:
            unfinished[completion[_]] += 1

    for _ in range(len(participant)):
        isExist = unfinished.get(participant[_])

        if isExist == None:
            return participant[_]
        else:
            unfinished[participant[_]] -= 1

        if unfinished[participant[_]] < 0:
            return participant[_]

if __name__ == "__main__":
    p = ["mislav", "stanko", "mislav", "ana"]
    c = ["stanko", "ana", "mislav"]
    print(solution(p, c))