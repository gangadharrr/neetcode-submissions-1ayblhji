class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            if mp.get(i, False):
                return True
            else:
                mp[i] = True
        return False