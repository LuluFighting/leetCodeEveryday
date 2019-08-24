import sys
MAXSIZE = sys.maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[ [0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices)+1)]
        for i in range(len(prices)+1):
            dp[i][0][0] = 0
            dp[i][0][1] = -MAXSIZE
        for i in range(3):
            dp[0][i][0] = 0
            dp[0][i][1] = -MAXSIZE
        for i in range(1,len(prices)+1):
            for k in range(1,3):
                dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i-1])
        return dp[-1][2][0]
