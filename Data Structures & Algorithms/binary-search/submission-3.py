class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 
        while left <= right:
            val = (left+right)//2
            if nums[val] == target:
                return val
            elif nums[val] < target:
                left = val+1
            else:
                right = val-1
        return -1
        