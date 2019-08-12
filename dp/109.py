import sys
INT_MAX = sys.maxsize
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        length  = len(triangle)
        for i in range(length-1):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i+1][j] += triangle[i][j]
                if j+1==len(triangle[i]):
                    triangle[i+1][j+1] += triangle[i][j]
                else:
                    triangle[i+1][j+1] += min(triangle[i][j],triangle[i][j+1])
        minret = INT_MAX
        for i in range(len(triangle[length-1])):
            if triangle[length-1][i] < minret:
                minret = triangle[length-1][i]
        return minret