class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0
        length = len(s)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i]=1
            if i+1<length:
                dp[i][i+1] = 2 if s[i]==s[i+1] else 0
        maxlen = 0
        for i in range(length):
            for j in range(i):
                if i-j<2:
                    continue
                if s[i]==s[j] and dp[j+1][i-1]>0:
                    dp[j][i] = 2+dp[j+1][i-1]
                    if dp[j][i]>maxlen:
                        maxlen = dp[j][i]
                else:
                    dp[j][i]=0
        return maxlen

    def longestPalindrome(self, s):
        # write your code here
        hashmap,maxlen = {},0
        for ch in s:
            if not ch in hashmap:
                hashmap[ch] = 0
            else:
                hashmap[ch]+=1
        hasOdd = False
        for ch in hashmap.keys():
            if hashmap[ch]%2 == 0:
                maxlen+=hashmap[ch]
            else:
                hasOdd = True
                maxlen+=hashmap[ch]-1
        if hasOdd==True:
            maxlen+=1
        return maxlen