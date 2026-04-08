class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(target, nums, left, right):
            if left == right:
                return left if nums[left] == target else -1
            elif left >= right: return -1
            else:
                val = (left + right)//2
                if nums[val] == target:
                    return val
                elif nums[val] < target:
                    return binarySearch(target, nums, val+1, right)
                else:
                    return binarySearch(target, nums, left, val)
        return binarySearch(target, nums, 0, len(nums)-1)
        