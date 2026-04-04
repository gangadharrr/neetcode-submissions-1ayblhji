class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        leftmx,rightmx = height[left], height[right]
        top_wall=-1
        out=0
        while left<right:
            if height[left] < height[right]:
                leftmx=max(leftmx, height[left])
                out+=(leftmx-height[left])
                left+=1
            else:
                rightmx=max(rightmx, height[right])
                out+=(rightmx-height[right])
                right-=1
        return out