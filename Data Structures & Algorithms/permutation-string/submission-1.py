class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i,0)+1
        temp={}
        for j in s2[:len(s1)]:
            if count.get(j, False):
                temp[j] = temp.get(j, 0) + 1
        if(temp==count):
            return True
        for i in range(1,len(s2)-(len(s1)-1)):
            if count.get(s2[i-1], False) and temp.get(s2[i-1],0):
                temp[s2[i-1]]-=1
            if count.get(s2[i+len(s1)-1], False):
                temp[s2[i+len(s1)-1]] = temp.get(s2[i+len(s1)-1],0)+1
            if(temp==count):
                return True
        return temp==count