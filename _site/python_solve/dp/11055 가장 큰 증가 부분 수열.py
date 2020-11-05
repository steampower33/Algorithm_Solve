import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0 for i in range(n+1)]
    sequence = [0 for i in range(n+1)]

    s = list(input().split())
    for i in range(1, n+1):
        sequence[i] = int(s[i-1])

    for i in range(1, n+1):
        dp[i] = sequence[i]
        for j in range(1, i):
            if sequence[j] < sequence[i] and dp[i] < dp[j] + sequence[i]:
                dp[i] = dp[j] + sequence[i]

    print(max(dp))
