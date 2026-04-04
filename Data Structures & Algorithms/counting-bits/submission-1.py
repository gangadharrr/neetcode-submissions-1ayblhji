class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        m=1
        for i in range(1,n+1):
            if (m<<1)<=i:
                m<<=1
            out.append(out[i^m]+1)
        return  out