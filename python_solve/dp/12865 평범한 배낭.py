import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rsplit())
    items = list()
    for i in range(n):
        w, v = map(int, sys.stdin.readline().rsplit())
        items.append([w,v])

    dp = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= items[i-1][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][k])