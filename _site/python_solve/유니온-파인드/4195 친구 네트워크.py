# 입/출력 빠르게.
import sys
input = sys.stdin.readline
print = sys.stdout.write

# 부모 찾기.
def getParent(graph, x):
    if graph[x] == x: return x
    graph[x] = getParent(graph, graph[x])
    return graph[x]

# 합집합 및 부모노드에 전체 길이 넣기.
def unionParent(graph, a, b, len):
    a = getParent(graph, a)
    b = getParent(graph, b)

    if a != b:
        # a가 무조건 부모로.
        graph[b] = a
        len[a] += len[b]
    return a

if __name__ == "__main__":
    # 그래프, 길이 설정.
    graph = dict()
    len = dict()

    for i in range(int(input())):
        for j in range(int(input())):
            # 기본 설정.
            a, b = input().split()
            if a not in graph:
                graph[a] = a
                len[a] = 1
            if b not in graph:
                graph[b] = b
                len[b] = 1
            # 합집합 및 부모 설정.
            p = unionParent(graph, a, b, len)
            print(str(len[p]))
            print("\n")
        graph.clear()
