class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i, j in zip(s, t):
            s_map[i] = s_map.get(i, 0) + 1
            t_map[j] = t_map.get(j, 0) + 1
        for i in s_map:
            if t_map.get(i, False) and t_map[i] == s_map[i]:
                continue
            else:
                return False
        return True