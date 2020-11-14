import sys

def dfs(cnt, last):
    global result

    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += stat[i][j]
                elif not visited[i] and not visited[j]:
                    link += stat[i][j]
        result = min(result, abs(start - link))

        return
    for i in range(last, N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, i+1)
            visited[i] = False

if __name__ == "__main__":
    N = int(input())
    stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    visited = [False] * N
    result = sys.maxsize

    dfs(0, 0)

    print(result)



