class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def mappings(s1, t1):
            #print(s1, t1)
            m = {}
            for i in range(len(s1)):
                if s1[i] in m and (m[s1[i]] != t1[i]):
                    return False
                m[s1[i]]=t1[i]
            return True
        
        return mappings(s, t) and mappings(t, s)