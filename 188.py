import sys
MAXSIZE = sys.maxsize
class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]
        dp[0][0],dp[0][1] = 0,-MAXSIZE
        for i in range(1,len(prices)+1):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i-1])

        return dp[-1][0]
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k> len(prices)//2:
            return self.maxProfit1(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices)+1)]
        for i in range(len(prices)+1):
            dp[i][0][0] = 0
            dp[i][0][1] = -MAXSIZE
        for i in range(k+1):
            dp[0][i][0] = 0
            dp[0][i][1] = - MAXSIZE
        for i in range(1,len(prices)+1):
            for j in range(1,k+1):
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i-1])
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i-1])
        return dp[-1][-1][0]