###0-1背包问题
class Solution:
    def backPack(self,costList,weightList,cost):
        dp = [[0 for _ in range(cost+1)] for _ in range(len(costList))]
        for i in range(cost+1):
            if costList[0]>i:
                dp[0][i] = 0
            else:
                dp[0][i] = weightList[0]
        for i in range(1,len(costList)):
            for j in range(cost+1):
                if j-costList[i]>=0:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-costList[i]]+weightList[i])
                else:  #放不下i物品
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[-1][cost]


obj = Solution()
print(obj.backPack([1,4,3],[1500,3000,2000],4))