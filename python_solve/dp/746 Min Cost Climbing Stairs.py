class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for _ in range(2, len(cost)):
            cost[_] += min(cost[_ - 1], cost[_ - 2])

        return min(cost[-1], cost[-2])
