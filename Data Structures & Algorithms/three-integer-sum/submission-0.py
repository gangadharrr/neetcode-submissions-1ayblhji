class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d={}
        out = []
        nums.sort()
        print(nums)
        for k in range(len(nums)-1):
            target = -nums[k]
            i, j = k+1, len(nums)-1
            while i!=j:
                if nums[i]+nums[j] == target:
                    if not d.get((nums[k], nums[i], nums[j]), False):
                        out.append([nums[k], nums[i],nums[j]])
                        d[(nums[k], nums[i], nums[j])] = 1
                    j-=1
                elif nums[i]+nums[j] > target:
                    j-=1
                else:
                    i+=1

        
        return out