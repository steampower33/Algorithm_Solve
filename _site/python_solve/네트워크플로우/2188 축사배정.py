
# 입력 빠르게
import sys
input = sys.stdin.readline

def dfs(x):
    for i in range(len(g[x])):
        y = g[x][i]
        if check[y]: continue
        check[y] = True
        if d[y] == 0 or dfs(d[y]):
            d[y] = x
            return True
    return False

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = {}
    for i in range(1, M+1):
        temp = list(map(int, input().split()))
        graph[i] = temp[1:]
    MAX = 201
    d = [0] * MAX
    check = [False] * MAX
    cnt = 0

    for i in range(1, N+1):
        check = [False] * MAX
        if dfs(i): cnt += 1
    print(cnt)

