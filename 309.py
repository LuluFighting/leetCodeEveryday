import sys
MAXSIZE = sys.maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]
        dp[0][0],dp[0][1] = 0,-MAXSIZE
        for i in range(1,len(prices)+1):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i-1])
            if i-2>=0:
                dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i-1])
            else:
                dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i-1])
        return dp[-1][0]