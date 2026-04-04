class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        nums.sort()
        maxval = 1
        val = 1
        for i in range(1, len(nums)):
            if nums[i-1]+1==nums[i]:
                val+=1
                maxval = max(maxval,val)
            elif nums[i-1]!= nums[i]:
                val = 1
        return maxval