
def solution(participant, completion):

    unfinished = {}
    result = None

    for _ in range(len(participant)):

        isExist = unfinished.get(participant[_])

        if isExist == None:
            unfinished[participant[_]] = 1
        else:
            unfinished[participant[_]] += 1

    print(unfinished)

    for _ in range(len(completion)):

        if unfinished[completion[_]] == 1:
            unfinished[completion[_]] -= 1
        elif unfinished[completion[_]] == 2:
            unfinished[completion[_]] -= 1

    for _ in range(len(participant)):
        if unfinished[participant[_]] == 1:
            return participant[_]

if __name__ == "__main__":
    p = ["leo", "kiki", "eden"]
    c = ["eden", "kiki"]
    print(solution(p, c))