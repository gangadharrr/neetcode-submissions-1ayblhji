class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fw = []
        bw = []
        fwp = 1
        bwp = 1
        for i in range(len(nums)):
            fwp*=nums[i]
            fw.append(fwp)
            bwp*=nums[len(nums)-1-i]
            bw.insert(0, bwp)
        out = []
        for i in range(len(nums)):
            if i==0 and i+1<len(nums):
                out.append(bw[i+1])
            elif i==len(nums)-1 and i-1 >=0:
                out.append(fw[i-1])
            else:
                out.append(fw[i-1] * bw[i+1])

        return out
        