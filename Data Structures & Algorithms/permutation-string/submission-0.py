class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i,0)+1
        for i in range(len(s2)):
            temp={}
            for j in s2[i:i+len(s1)]:
                temp[j] = temp.get(j, 0) + 1
            if(temp==count):
                return True
        return False