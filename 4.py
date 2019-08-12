import sys
INT_MAX = sys.maxsize
INT_MIN = -INT_MAX


class Solution:
    def findMedianSortedArrays(self, nums1, nums2 ):
        if nums1 is None:
            return nums2[len(nums2)//2] if len(nums2)%2==1 else (nums2[len(nums2)//2] + nums2[len(nums2)//2-1])/2.0
        elif nums2 is None:
            return nums1[len(nums1)//2] if len(nums1)%2==1 else (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2.0
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        left,right = 0,2*len(nums1)
        lmax1,lmax2,rmin1,rmin2 = 0,0,0,0
        while left <= right:
            c1 = left + (right-left)//2
            c2 = len(nums1)+len(nums2) - c1
            lmax1 = INT_MIN if c1 == 0 else nums1[(c1-1)//2]
            rmin1 = INT_MAX if c1 == 2*len(nums1) else nums1[c1//2]
            lmax2 = INT_MIN if c2 == 0 else nums2[(c2-1)//2]
            rmin2 = INT_MAX if c2 == 2*len(nums2) else nums2[c2//2]
            if lmax1>rmin2:
                right = c1-1
            elif lmax2>rmin1:
                left = c1+1
            else:
                break
        return (max(lmax1,lmax2)+min(rmin1,rmin2))/2.0

obj = Solution()
print(obj.findMedianSortedArrays([1,3],[2]))