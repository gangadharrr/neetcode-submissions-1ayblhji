class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tsm = n*(n+1)>>1
        sm = sum(nums)
        return tsm - sm
        