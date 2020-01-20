

# field에 들어있는 값의 r위치가 이미 한번 돌았던거라면, 또 돌필요가 없다.
# 이분 매칭에서는 이미 있는 곳을 선택하려할때 이미 다른게 있으면
# 그 다른걸 가지고 또 다른 가능성이 있는지 탐색하는데
# 이 문제에서는 돌 한번 치우면 끝이기 때문에 또 치울 필요가없다.
# 그러니 field를 길이 만큼 돌면서, 되면 ans += 1 해주고 안되면 아무것도 안해주면된다.
def dfs(a):
    global v,r,field
    if v[a]:
        return 0
    v[a] = 1
    for b in field[a]:
        if r[b] == -1 or dfs(r[b]):
            r[b] = a
            return 1
    return 0

if __name__ == "__main__":
    # 격자, 돌멩이.
    n, k = map(int, input().split())

    # 운동장.
    field = [[] for i in range(n)]

    # 돌맹이 위치.
    for i in range(k):
        a, b = map(int, input().split())
        field[a - 1].append(b - 1)

    # n 만큼을 돌면서 확인해주면된다.
    v = [0] * n
    r = [-1] * n

    ans = 0
    for i in range(n):
        v = [0] * n
        ans += dfs(i)
    print(ans)
