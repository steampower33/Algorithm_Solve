import sys
from collections import defaultdict, deque
INF = sys.maxsize

#bfs
def bfs(start, sink, parent):
    visited = defaultdict(lambda:0)
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        u = queue.popleft()
        for ind in pipe[u]:
            val = pipe[u][ind]
            # 방문한적 있으면 넘김.
            if visited[ind]:
                continue
            # 값이 - 이면 넘김.
            if val <= 0:
                continue
            queue.append(ind)
            visited[ind] = 1
            parent[ind] = u
    return 1 if visited[sink] else 0

#ford_fulkerson
def ford_fulkerson(start, sink):
    parent = defaultdict(lambda:-1)
    max_flow = 0
    while bfs(start, sink, parent):
        path_flow = INF
        s = sink
        #최소를 찾고 찾으면 max_flow에 더해줌
        while s!=start:
            path_flow = min(path_flow, pipe[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        #유량의 오고감으로 빼주고 더함으로써 그 통로의 유량을 설정.
        while v!=start:
            u = parent[v]
            pipe[u][v] -= path_flow
            pipe[v][u] += path_flow
            v = parent[v]
    return max_flow

if __name__ == "__main__":

    sys.setrecursionlimit(10 ** 6)

    # 네트워크 유량에서 방향이 없으므로
    # 양쪽 유량을 같은 값으로 초기화
    k = int(input())
    for i in range(k):
        n, m = map(int, input().split())
        pipe = defaultdict(lambda: defaultdict(int))
        for i in range(m):
            a, b, c = map(int, input().split())
            pipe[a][b] += c
            pipe[b][a] += c

        print(pipe)

        print(ford_fulkerson(1, n))

        print(pipe)