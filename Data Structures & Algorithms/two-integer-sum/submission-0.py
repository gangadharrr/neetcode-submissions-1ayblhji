class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if d.get(target-nums[i], -1)>=0:
                return [d.get(target-nums[i]), i]
            else:
                d[nums[i]] = i
        