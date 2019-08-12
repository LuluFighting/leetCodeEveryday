class Solution:
    def minNumofremoveN(self,s,n):
        length = len(s)
        if length-n<=0:
            return 0
        dp = ['']*(n+1)
        dp[0] = list(s)
        for i in range(1,n+1):
            if int(dp[i-1][0]) > int(dp[i-1][1]):
                dp[i] = dp[i-1][:]
                dp[i].pop(0)
                continue
            j = 0
            for j in range(1,len(dp[i - 1])):
                if j+1<len(dp[i-1]):
                    if dp[i-1][j]>= dp[i-1][j-1] and dp[i-1][j]>= dp[i-1][j+1]:
                        break
            dp[i] = dp[i-1][:]
            dp[i].pop(j)
        return ''.join(dp[n])

obj = Solution()
print(obj.minNumofremoveN('2357248513',4))