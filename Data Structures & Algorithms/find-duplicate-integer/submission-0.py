class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if mp.get(i, False):
                return i
            else:
                mp[i] = True
        