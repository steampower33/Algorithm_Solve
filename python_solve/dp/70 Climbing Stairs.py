class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]

        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2

        for _ in range(3, n+1):
            dp[_] = dp[_-1] + dp[_-2]

        return dp[n]


s = Solution()

print(s.climbStairs(5))