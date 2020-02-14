# 입력 및 무한대 그래프 설정.
n, m, x = map(int, input().split())
INF = 987654321
graph = [[INF for i in range(n)]for j in range(n)]

# 방향 입력 가중치 설정.
for i in range(m):
    x, y, v = map(int, input().split())
    graph[x-1][y-1] = v

# 자시자신으로는 못감.
for i in range(n):
    graph[i][i] = 0

v = [0 for i in range(n)]
d = [0 for i in range(n)]

def getSmallIndex():
    min = INF
    index = 0
    for i in range(n):
        if d[i] < min:
            if not v[i]:
                min = d[i]
                index = i
    return index

def dijkstra(start, graph, v, d):
    for i in range(n):
        d[i] = graph[start][i]

    v[start] = True
    for i in range(n-2):
        current = getSmallIndex()
        v[current] = True
        for j in range(n):
            if not v[j]:
                if d[current] + graph[current][j] < d[j]:
                    d[j] = d[current] + graph[current][j]

dijkstra(0, graph, v, d)
for i in range(n):
    print(d[i], end=" ")