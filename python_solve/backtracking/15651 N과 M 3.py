def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(i+1)
        dfs(depth+1,n,m)
        result.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = list()
    dfs(0, n, m)