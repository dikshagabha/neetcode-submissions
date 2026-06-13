class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        res=0
        for r in range(1, len(s)):
            res+=abs(ord(s[l]) - ord(s[r]))
            l+=1
        return res