class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, flag, buy = 0, 0, 10**10
        if len(prices) <= 1:
            return 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i] and not flag:
                    flag = 1
                    buy = prices[i]
            else:
                if flag:
                    ans += prices[i] - buy
                    if prices[i+1] > prices[i]:
                        buy = prices[i]
                        flag = 1
                    else:
                        flag = 0
                        buy = 10 ** 10
        if prices[i+1] > prices[i]:
            ans += prices[i+1] - buy
        return ans
                    