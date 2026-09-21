class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        keys = {}
        vals = []
        res = ''
        for i in range(len(s)):
            if s[i] in vals:
                res+=keys[s[i]]
                continue
            if pattern[i] in keys.values():
                return False
            keys[s[i]] = pattern[i]
            vals.append(s[i])
            res+=keys[s[i]]
        print(res)
        return res==pattern
