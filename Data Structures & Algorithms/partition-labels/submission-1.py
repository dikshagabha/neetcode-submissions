class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        
        l = 0
        res= []
        while l<len(s):
            r = l
            c = 0
            req=0
            while r<len(s):
                counts[s[r]]-=1
                if s[r] not in s[l:r]:
                    c+=1
                if counts[s[r]]==0:
                    req +=1
                if req == c:
                    break
                r+=1
            #print(l, r, s[l:r+1])
            res.append(r-l+1)
            l=r+1
        return res