class Solution:
    def superPow(self, a: int, b) -> int:
        listLen = len(b)
        res = 1
        if a==1:
            return 1
        a = a%1337
        for i in range(listLen):
            thisRound = self.compute(a,b[i])
            res = (self.compute(res,10) * thisRound)%1337
        return int(res)
    def compute(self,a,bNum):
        if bNum==0:
            return 1
        if bNum==1:
            return (a)%1337
        if bNum%2==0:
            return (self.compute(a,bNum/2) * self.compute(a,bNum/2))%1337
        else:
            return ((self.compute(a,(bNum-1)/2) * a)%1337 * self.compute(a,(bNum-1)/2))%1337
obj = Solution()
print(obj.superPow(1,[4,3,3,8,5,2]))