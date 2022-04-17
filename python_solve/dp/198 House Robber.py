class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        dp = [nums[_] for _ in range(len(nums))]
        for _ in range(1, len(nums)):
            if _ == 1:
                dp[1] = max(dp[0], dp[1])
            else:
                dp[_] = max(dp[_ - 1], dp[_ - 2] + nums[_])

        return dp[-1]