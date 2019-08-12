class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[nums[0]]]
        hashmap = {nums[0]:0}
        for i in range(1,len(nums)):
            if nums[i] not in hashmap.keys():
                hashmap[nums[i]] = len(res)
                res += [ res[j] + [nums[i]]  for j in range(len(res)) if res[j][-1]<=nums[i] ]  + [[nums[i]]]
            else:
                length = hashmap[nums[i]]
                hashmap[nums[i]] = len(res)
                res += [ res[j] + [nums[i]] for j in range(length,len(res)) if res[j][-1]<=nums[i]]


        return [res[j] for j in range(len(res)) if len(res[j])>=2]

