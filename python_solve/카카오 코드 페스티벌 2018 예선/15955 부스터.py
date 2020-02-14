import math

# 두 지점 거리 구하기.
def distance(a, b):
    x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
    dist = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    return dist

# 시작지를 제외한 목적지에서 가장 가까운 체크포인트.
def all_dist(cp, start, end):
    dist = list()
    for i in range(1, len(cp)+1):
        if i == start or i == end: continue
        dist.append((i, distance(cp[i],cp[end])))
    return dist

if __name__ == "__main__":
    n, q = map(int, input().split())
    cp = dict()
    check_boost = [1 for i in range(n+1)]

    for i in range(1, n+1):
        x, y = map(int, input().split())
        cp[i] = (x,y)

    for i in range(q):
        start, end, hp = map(int, input().split())
        # 부스트, 최대 체력 설정.
        boost = 1
        max_hp = hp
        can_loop = True
        # 바로 갈수있으면 가능.
        if distance(cp[start],cp[end]) <= hp: print("YES")
        else:
            while can_loop == True:
                print(start)
                if start == end:
                    print("YES")
                    break
                # end에서 가까운 순서대로.
                dist = all_dist(cp, start, end)
                dist = sorted(dist, key=lambda x: x[1])
                # start에서 가까운 순서.
                s_dist = all_dist(cp, 0, end)
                s_dist = sorted(s_dist, key=lambda x: x[1])

                # print(dist)
                # print(cp[start])
                # print(cp[dist[0][0]])

                # 가로 세로 둘 중 하나 평행 한지.
                # 평행하면 체크포인트 이동.
                tmp = start
                for i in dist:
                    if tmp != start: continue
                    if tmp == end:
                        print("YES")
                        break
                    if cp[start][0] == cp[i[0]][0] or cp[start][1] == cp[i[0]][1]:
                        start = i[0]
                        break
                    else:
                        for i in s_dist:
                            if i[1] < hp:
                                start = i[0]
                                break
                dist.clear()



'''
5 3
1 2
3 2
4 4
6 2
3 9
1 5 0
3 4 0
3 4 2
'''