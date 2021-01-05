def solve(n):

    if dp.get(n) != None:
        return dp[n]
    else:
        if n % 2:
            newN = (n + 1) // 2
            result = solve(newN) ** 2 + solve(newN - 1) ** 2
            dp[n] = result % 1000000007
            return dp[n]
        else:
            newN = n // 2
            result = (solve(newN - 1) * 2 + solve(newN)) * solve(newN)
            dp[n] = result % 1000000007
            return dp[n]

if __name__ == "__main__":
    n = int(input())
    dp = {0: 0, 1: 1, 2: 1}

    print(solve(n))
