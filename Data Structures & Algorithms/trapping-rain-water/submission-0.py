class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        out=0
        while left<right:
            top_wall=min(height[left], height[right])
            for i in range(left,right+1):
                if height[i]<top_wall:
                    out+=(top_wall-height[i])
                    height[i]=top_wall
            while left<len(height):
                if height[left]>top_wall:
                    break
                left+=1
            while right>=0:
                if height[right]>top_wall:
                    break
                right-=1
        return out


