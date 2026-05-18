class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        countt = {}
        for i in t:
            countt[i] = countt.get(i,0)+1
        
        l,r=0,0
        counts={} 
        have, need = 0, len(countt)
        res = [-1, -1]
        reslen =float("infinity") 
        while r<len(s):
            
            counts[s[r]] = counts.get(s[r],0)+1
            if s[r] in countt and counts[s[r]]==countt[s[r]]:
                have+=1
            
            while have==need:
                if reslen> r-l+1:
                    reslen = r-l+1
                    res = [l, r]
                
                counts[s[l]]-=1

                if s[l] in countt and counts[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
            r+=1
        return s[res[0]:res[1]+1]
                
            
