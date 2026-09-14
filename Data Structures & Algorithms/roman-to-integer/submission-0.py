class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {"I": 1,"V": 5,
                    "X":             10,
                    "L":             50,
                    "C":             100,
                    "D":             500,
                    "M":             1000
                    }
        
        values_allowed = {'I': ['V', 'X'], 'X' : ['L', 'C'], 'C':['D','M']}
        i=0
        res = 0
        while i<len(s):
            cur = s[i]
            if i<len(s)-1 and cur in values_allowed.keys() and s[i+1] in values_allowed[cur]:
                res += values[s[i+1]]-values[cur]
                i+=2
                continue
            res+=values[cur]
            i+=1
        return res
