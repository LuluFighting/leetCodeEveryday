class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        queue = [(0,0)]
        memo = [0]*(n+1)
        while len(queue)!=0:
            curNum = queue.pop(0)
            j=1
            while curNum[0]+j*j<=n:
                if curNum[0]+j*j == n:
                    return curNum[1]+1
                if memo[curNum[0]+j*j] == 0:
                    queue.append((curNum[0]+j*j,curNum[1]+1))
                    memo[curNum[0]+j*j]=1
                j+=1
import sys
MAXSIZE = sys.maxsize
class Solution2:
    def numSquares(selfs,n):
        dp = [MAXSIZE]*(n+1)
        dp[0],dp[1] = 0,1
        for i in range(n+1):
            j=0
            while i+j*j<=n:
                dp[i+j*j] = min(dp[i+j*j],dp[i]+1)
                j+=1
        return dp[n]

obj = Solution2()
print(obj.numSquares(12))