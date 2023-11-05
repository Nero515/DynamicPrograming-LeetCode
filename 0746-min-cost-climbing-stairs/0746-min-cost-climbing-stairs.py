class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sum_cost = [0] * len(cost)
        sum_cost[0] = cost[0]
        sum_cost[1] = cost[1]
        
        for i in range(2, len(cost)):
            sum_cost[i] = min(sum_cost[i-2], sum_cost[i-1]) + cost[i]
        
        return min(sum_cost[-1], sum_cost[-2])