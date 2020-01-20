# 정점, 간선, 시작할 정점
n, m, v = map(int, input().split())

# 그래프 생성
graph = dict()

# 빈 리스트([]) 를 가지는 정점을 설정.
for i in range(1, n+1):
    graph[i] = []

# 간선을 연겨하는 두 정점의 번호를 받고,
# 두 정점을 연결한다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
# 선입후출.
# 깊이 우선 탐색이므로, 트리로 따지면, 맨 왼쪽에꺼부터 계속해서 탐색하며 내려간다.

def dfs(graph, start):
    visit = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for _ in graph[node]:
                stack.extend(reversed(graph[node]))
    return visit

# bfs
# 선입후출.
# 너비 우선 탐색이므로, 트리로 따지면, 그 층을 탐색 다할때까지 탐색하고 내려간다.
def bfs(graph, start):
    visit = list()
    queue = list()

    queue.append(start)
    while queue:
        node  = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

# 각 정점에 연결되어 있는 정점들은 정렬되어있어야한다.
for i in range(1, n+1):
    graph[i].sort()

# dfs 및 bfs 실행한 결과 출력.
for i in dfs(graph,v):
    print(i,end=" ")

print()

for i in bfs(graph,v):
    print(i, end=" ")