class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            if d.get(tuple(sorted(i)), []) != []:
                d.get(tuple(sorted(i))).append(i)
            else:
                d[tuple(sorted(i))] = d.get(tuple(sorted(i)), []) + [i]
        return list(d.values())
