class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid)==0 or len(obstacleGrid[0])==0:
            return 0
        m,n= len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,m):
            if obstacleGrid[i][0]==1:
                for j in range(i,m):
                    dp[j][0] = 0
                break
            dp[i][0]= 1
        for j in range(0,n):
            if obstacleGrid[0][j]==1:
                for k in range(j,n):
                    dp[0][k]=0
                break
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif obstacleGrid[i-1][j]==1:
                    dp[i][j] = 0 if obstacleGrid[i][j-1]==1 else dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j-1]==1 else dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
obstacleGrid = [[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
obj = Solution()
print(obj.uniquePathsWithObstacles(obstacleGrid))