class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sm=0
        for i in nums:
            sm^=i
        return sm