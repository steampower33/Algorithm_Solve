import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0 for i in range(100001)]
    for i in range(n+1): dp[i] = i
    for i in range(2, n+1):
        for j in range(2, i):
            if j*j > i: break
            dp[i] = min(dp[i], dp[i - j*j] + 1)

    print(dp[n])