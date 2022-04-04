from itertools import combinations

def solution(clothes):
    c = dict()
    cnt = list(0 for i in range(30))
    result = 0

    idx = 0
    for _ in clothes:
        kind = c.get(_[1])
        if kind == None:
            c[_[1]] = idx
            cnt[c[_[1]]] = 1
            idx += 1
        else:
            cnt[c[_[1]]] += 1

    result += sum(cnt[:idx])
    for r in range(2, idx + 1):
        l = list(combinations(cnt[:idx], r))
        for n in l:
            m = 1
            for j in n:
                m *= j
            result += m

    return result

if __name__ == "__main__":
    input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["glasses", "eyewear"], ["green", "clothes"]]
    #input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "asdf"]]

    solution(input)