class Solution:
    def reverseBits(self, n: int) -> int:
        sm=0
        count=0
        while n:
            if count>=31:
                sm|=(n&1)
                break
            sm|=(n&1)
            sm<<=1
            n>>=1
            count+=1
        excount = 31-count
        while excount>0:
            sm<<=1
            excount-=1
        return sm