import sys
input = sys.stdin.readline

if __name__ == "__main__":
    tc = int(input())

    for i in range(tc):
        dp = [[0 for i in range(100001)] for j in range(2)]
        stickers = [[0 for i in range(100001)] for j in range(2)]
        n = int(input())
        for j in range(2):
            s = list(map(int, input().split()))
            for k in range(1 , n+1):
                stickers[j][k] = s[k-1]
        dp[0][1] = stickers[0][1]
        dp[1][1] = stickers[1][1]

        for j in range(2, n+1):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + stickers[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + stickers[1][j]

        rtn = max(dp[0][n], dp[1][n])

        print(rtn)