def solution(clothes):
    c = dict()
    cnt = list(0 for i in range(30))
    result = 1

    idx = 0
    for _ in clothes:
        kind = c.get(_[1])
        if kind == None:
            c[_[1]] = idx
            cnt[c[_[1]]] = 1
            idx += 1
        else:
            cnt[c[_[1]]] += 1

    result = 1
    for _ in cnt[:idx]:
        result *= _+1

    return result - 1

if __name__ == "__main__":
    input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["glasses", "eyewear"], ["green", "clothes"]]
    #input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "asdf"]]

    print(solution(input))