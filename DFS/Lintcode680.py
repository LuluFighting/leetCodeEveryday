class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if not s:
            return [[]]
        ret = []
        def split(start=0,res=[]):
            if start == len(s):
                ret.append(res)
            for i in range(1,3):
                if start+i < len(s):
                    res.append(s[start:start+i])
                    split(start+i,res[:])
                    res.pop()
        split(0)
        return ret
