class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i,0)+1
        temp={s2[0]:1}
        i,j=0,0
        while j<len(s2)-1:
            if temp == count:
                return True
            if ((j+1)-i) == len(s1):
                temp[s2[i]] = temp.get(s2[i], 0) - 1
                if temp[s2[i]] <=0 :
                    del temp[s2[i]]
                i+=1
                j+=1
                temp[s2[j]] = temp.get(s2[j], 0) + 1
            else:
                j+=1
                temp[s2[j]] = temp.get(s2[j], 0) + 1
        return temp==count