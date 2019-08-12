class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        p0,p2 = 0,len(nums)-1
        i=0
        while i<=p2:
            if nums[i]==0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0+=1
                i+=1
            elif nums[i]==2:
                nums[p2],nums[i] = nums[i],nums[p2]
                p2-=1
            else:
                i+=1
