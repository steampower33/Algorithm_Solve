

# bfs
# 방문, q 설정.
# q에 시작위치 넣고.
# q가 빌때까지 돈다.
# node에 q의 값을 pop(0)하고
# 그 pop 한 값이 방문한적없다면 visit에 넣고
# q에 graph[node] 값을 마지막에 넣어준다.
def bfs(graph, start):
    visit = list()
    queue = list()

    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

if __name__ == "__main__":
    # 컴퓨터 수.
    computers = int(input())
    # 쌍 수.
    pair = int(input())

    # 그래프.
    graph = dict()

    # 그래프 설정.
    for i in range(1, computers+1):
        graph[i] = []

    # 그래프 양방향 연결.
    for i in range(pair):
        one, two = map(int, input().split())
        graph[one].append(two)
        graph[two].append(one)

    # 바이러스 걸린 컴퓨터 수 넣을 곳.
    birus = list()

    # 시작위치를 1 ~ 컴퓨터 수 만큼 돌아서 birus에 길이를 넣는다.
    for i in range(1, computers+1):
        result = bfs(graph, i)
        birus.append(len(result)-1)

    # 그 중 최대 값을 출력한다.
    print(max(birus))

