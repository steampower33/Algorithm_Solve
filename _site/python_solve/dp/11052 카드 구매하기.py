import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0] * 1001
    p = [0] * 1001
    s = list(map(int, input().split()))
    for i in range(1, n+1):
        p[i] = s[i-1]

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j] + p[j])

    print(dp[n])




