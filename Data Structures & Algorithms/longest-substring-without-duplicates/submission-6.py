class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        mx = 1
        left = 0
        right = 1
        d={s[left]:0}
        while right < len(s):
            if d.get(s[right], -1) != -1:
                left = d.get(s[right]) + 1
                d = {s[i]:i for i in range(left,right+1)}
            else:
                d[s[right]] = right
                mx = max(mx, right+1-left)
            right+=1
        return mx


        