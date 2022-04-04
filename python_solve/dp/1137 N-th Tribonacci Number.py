class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribo = [0 for _ in range(n+1)]
        if n >= 1:
            tribo[1] = 1
        if n >= 2:
            tribo[2] = 1

        for _ in range(3, n+1):
            tribo[_] = tribo[_-3] + tribo[_-2] + tribo[_-1]

        return tribo[n]

a = Solution()

print(a.tribonacci(4))