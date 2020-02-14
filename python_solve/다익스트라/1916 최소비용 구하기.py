from heapq import heappush, heappop
INF = 987654321

if __name__ == "__main__":
    # 도시의 개수.
    N = int(input())
    # 버스의 개수.
    M = int(input())

    dist = [0 for i in range(N)]
    graph = dict()
    for i in range(N):
        graph[i+1] = list()

    for i in range(M):
        city1, city2, cost =  map(int , input().split())
        graph[city1].append((city2,cost))

    print(graph)