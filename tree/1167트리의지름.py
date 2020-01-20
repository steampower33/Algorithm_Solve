lines = int(input())

graph = dict()

for i in range(lines):
    graph[i+1] = dict()

#print(bfs_dfs)

for i in range(0, lines):
    info = input().split()
    j = 1
    first = int(info[0])
    while j < len(info)-1:
        graph[first][int(info[j])] = int(info[j+1])
        j += 2

for i in range(1, len(graph)+1):
    for j in range(len(graph[i])):
        if graph[i] == graph[i+1]:
            print(0)

print(graph)