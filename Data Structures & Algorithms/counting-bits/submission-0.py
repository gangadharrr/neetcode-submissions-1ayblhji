class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            k=i
            sm=0
            while k:
                sm+=(k&1)
                k>>=1
            out.append(sm)
        return  out