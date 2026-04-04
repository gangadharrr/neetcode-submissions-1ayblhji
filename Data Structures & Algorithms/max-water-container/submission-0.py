class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        mxval=-1
        while(i<j):
            mxval = max(mxval, min(heights[i], heights[j])*(j-i))
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return mxval
        