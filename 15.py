class Solution:
    def threeSum(self, nums):
        if nums is None or len(nums)==0:
            return []
        ret = []
        nums.sort()
        if nums[0]>0:
            return []
        def twoSum(nums,start,target,res=[]):
            left,right = start,len(nums)-1
            while left<right:
                while left-1>=start and left<len(nums) and nums[left]==nums[left-1]:
                    left+=1
                while right+1<len(nums) and right>=0 and nums[right]==nums[right+1]:
                    right-=1
                if left>=len(nums) or right<0 or left>=right:
                    break
                if nums[left]+nums[right] == target:
                    res.append([nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[left] + nums [right] > target:
                    right-=1
                else:
                    left+=1
            return res
        i=0
        while i<len(nums):
            if i-1>=0 and nums[i-1]==nums[i]:
                i+=1
                continue
            twoRes = twoSum(nums,i+1,-nums[i],[])
            if len(twoRes)!=0:
                for twores in twoRes:
                    twores.append(nums[i])
                    ret.append(twores)
            i+=1
        return ret

obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))