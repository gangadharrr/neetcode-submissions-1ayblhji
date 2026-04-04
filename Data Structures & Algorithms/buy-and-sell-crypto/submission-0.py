class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        left = right = 0
        while right < len(prices):
            maxVal = max(maxVal, prices[right]-prices[left])
            if prices[left] > prices[right]:
                left = right
            right+=1
        return maxVal
        