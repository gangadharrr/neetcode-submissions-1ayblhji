class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = {}
        for k in range(len(nums)):
            target = -nums[k]
            i, j = k+1, len(nums)-1
            while i<j:
                if nums[i]+nums[j] == target:
                    if out.get((nums[k], nums[i], nums[j]), []) == []:
                        out[(nums[k], nums[i],nums[j])] = [nums[k], nums[i],nums[j]]
                    j-=1
                elif nums[i]+nums[j] > target:
                    j-=1
                else:
                    i+=1
        return list(out.values())
        