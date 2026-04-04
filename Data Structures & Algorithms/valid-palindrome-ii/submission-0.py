class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 2:
            return True
        def checkPal(i,j, exp):
            if i>=j:
                return True
            else:
                if s[i]==s[j]:
                    return checkPal(i+1,j-1, exp)
                elif exp:
                    return checkPal(i+1,j, False) or checkPal(i,j-1, False)
                else:
                    return False
        return checkPal(0,len(s)-1, True)
