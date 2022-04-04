import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    print(collections.Counter(participant))
    print(collections.Counter(completion))
    return list(answer.keys())[0]

if __name__ == "__main__":
    p = ["mislav", "stanko", "mislav", "ana"]
    c = ["stanko", "ana", "mislav"]
    print(solution(p, c))