class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## using one hashmap instead of 2
        cs = {}
        # matches, total = 0, len(s)

        if len(s) != len(t):
            return False
        
        for i in s:
            cs[i] = cs.get(i, 0)+1
        
        for j in t:
            if j not in cs.keys():
                return False
            cs[j]-=1
        
        for k, v in cs.items():
            if v!=0:
                return False
        
        return True
