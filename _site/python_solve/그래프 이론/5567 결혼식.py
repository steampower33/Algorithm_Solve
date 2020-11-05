
# 뿌리가 1인 그래프에서 1 다음 그 다음 까지의 값들을 중복없이 v에 넣어준다.
# 제한적인 구조이며 재활용이 어렵다.
def bfs(f):
    v = list()
    q = list()

    q.extend(f[1][1])
    for i in f[1][1]:
        q.extend(f[1][i])

    while q:
        node = q.pop(0)

        if node not in v:
            v.append(node)
    return v


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    # f[1]안에서 다 연결된다. 즉 1이 무조건 뿌리라고 설정함.
    friend = dict()
    friend[1] = dict()

    # 아래로는 그래프 설정이다.
    for i in range(1, m+1):
        friend[1][i] = list()

    for i in range(m):
        a, b = map(int, input().split())
        friend[1][a].append(b)
        friend[1][b].append(a)

    print(len(bfs(friend))-1)

