class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        mini = 101

        for i in range(len(prices)):
            maxp = max(prices[i]-mini, maxp)
            mini = min(mini, prices[i])

        return maxp
        