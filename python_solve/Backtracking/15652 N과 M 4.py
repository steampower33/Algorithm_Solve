def dfs(depth, last, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(last, n):
        if not visited[i]:
            result.append(i+1)
            dfs(depth + 1, i, n, m)
            visited[i] = False
            result.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False] * n
    result = list()
    dfs(0, 0, n, m)