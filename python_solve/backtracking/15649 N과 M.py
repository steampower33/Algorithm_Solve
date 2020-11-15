import sys

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            dfs(depth + 1, n, m)
            visited[i] = False
            result.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rsplit())
    visited = [False] * n
    result = list()
    dfs(0, n, m)

