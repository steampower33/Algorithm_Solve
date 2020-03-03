import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    line_sum = 0
    value = 0
    dp = [[0 for i in range(10)] for j in range(1001)]
    for i in range(10): dp[1][i] = 1

    for i in range(2, 1001):
        for j in range(10):
            if j == 0:
                for k in range(10): line_sum += dp[i-1][k]
                dp[i][j] = line_sum
                line_sum = 0
            else:
                dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]

    for i in range(10):
        value += dp[n][i]
        value = value % 10007

    print(value)