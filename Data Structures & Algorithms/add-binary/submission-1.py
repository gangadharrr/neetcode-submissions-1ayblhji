class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'
        sm = []
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0:
            if i>=0 and j>=0:
                if a[i] == '1' and b[j] == '1':
                    sm.insert(0,'0' if carry == '0' else '1')
                    carry = '1'
                elif a[i] == '1' or b[j] == '1':
                    sm.insert(0,'1' if carry == '0' else '0')
                else:
                    sm.insert(0, carry)
                    carry = '0'
                i-=1
                j-=1
            elif i>=0:
                if a[i] == '1' and carry == '1':
                    sm.insert(0,'0')
                elif a[i] == '1' or carry == '1':
                    sm.insert(0,'1')
                    carry = '0'
                elif carry == '1':
                    sm.insert(0, '1')
                    carry = '0'
                else:
                    sm.insert(0, '0')
                i-=1
            elif j>=0:
                if b[j] == '1' and carry == '1':
                    sm.insert(0,'0')
                elif b[j] == '1' or carry == '1':
                    sm.insert(0,'1')
                    carry = '0'
                elif carry == '1':
                    sm.insert(0, '1')
                    carry = '0'
                else:
                    sm.insert(0, '0')
                j-=1
        if carry == '1':
            sm.insert(0,'1')
        return ''.join(sm)