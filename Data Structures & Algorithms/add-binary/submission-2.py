class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a
        x,y=1,1
        for i in range(1,len(a)):
            x<<=1
            if a[i]=='1':
                x|=1
        for i in range(1,len(b)):
            y<<=1
            if b[i]=='1':
                y|=1
        sm = x+y
        out =[]
        while sm:
            out.insert(0, str(sm&1))
            sm>>=1
        return ''.join(out)