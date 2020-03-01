import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    sum = 0
    dp = [[0 for i in range(10)] for j in range(101)]

    for i in range(1, 10):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % (10 ** 9)

    for i in dp[n-1]:
        sum = (sum + i) % (10 ** 9)

    print(sum)