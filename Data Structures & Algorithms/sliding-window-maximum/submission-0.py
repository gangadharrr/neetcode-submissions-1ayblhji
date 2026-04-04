import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = [-nums[i] for i in range(k)]
        count={nums[0]:1}
        heapq.heapify(max_list)
        out=[-max_list[0]]
        for i in range(1,len(nums)-(k-1)):
            while max_list and count.get(-max_list[0], False):
                count[-max_list[0]] = count.get(-max_list[0], 0)-1
                if count[-max_list[0]]<=0:
                    del count[-max_list[0]]
                heapq.heappop(max_list)
            count[nums[i]] = count.get(nums[i], 0) + 1
            heapq.heappush(max_list, -nums[i+(k-1)])
            out.append(-max_list[0])
        return out