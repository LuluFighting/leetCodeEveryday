class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,m):
            dp[i][0]=1
        for j in range(0,n):
            dp[0][j]=1
        dp[0][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]