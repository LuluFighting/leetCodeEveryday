class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        tmpS = ['#']
        for i in range(len(s)):
            tmpS.append(s[i])
            tmpS.append('#')
        dp = [[1 for j in range(len(tmpS))] for i in range(len(tmpS))]
        mid = len(s)
        i = mid
        while i>
obj = Solution()
obj.longestPalindromeSubseq('hello')