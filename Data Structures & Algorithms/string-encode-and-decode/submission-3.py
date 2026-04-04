class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in range(len(strs)):
            s += str([ord(n) for n in strs[i]])+":"

        return s

    def decode(self, s: str) -> List[str]:
        out = []
        for words in s.strip(":").split(":"):
            if words:
                word = ''
                for letter in words.lstrip('[').rstrip(']').split(', '):
                    if letter:
                        word+=chr(int(letter))
                out.append(word)
        return out