class Solution:
    def hammingWeight(self, n: int) -> int:
        sm=0
        while n:
            sm+=(n&1)
            n>>=1
        return sm
        