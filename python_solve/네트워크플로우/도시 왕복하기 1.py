def dfs(way, graph, start):
    stack = list(); visit = list(); stack.append(start)
    while stack:
        node = stack.pop()
        if node == 2 or list(visit) not in way: return 1, visit
        if node not in visit:
            visit.append(node); stack.extend(reversed(graph[node]))
    return 0

if __name__ == "__main__":
    n, p = map(int, input().split()); graph = dict(); c=0; way = list()
    for i in range(1, n + 1): graph[i] = list()

    for i in range(p):
        a, b = map(int, input().split()); graph[a].append(b)

    for i in graph[1]:
        c_, v = dfs(way, graph, i); way.append(v); c += c_

    print(c)

