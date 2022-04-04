from itertools import combinations

def solution(clothes):
    c = dict()
    cnt = list()
    result = 0

    for _ in clothes:
        if c.get(_[1]) == None:
            c[_[1]] = 1
        else:
            c[_[1]] += 1

    for _ in c:
        cnt.append(c[_])

    for r in range(1, len(cnt) + 1):
        l = list(combinations(cnt, r))
        if r == 1:
            for n in l:
                result += n[0]
        elif r >= 2:
            for n in l:
                m = 1
                for j in n:
                    m *= j
                result += m

    return result

if __name__ == "__main__":
    #input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["glasses", "eyewear"], ["green", "clothes"]]
    input = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

    print(solution(input))