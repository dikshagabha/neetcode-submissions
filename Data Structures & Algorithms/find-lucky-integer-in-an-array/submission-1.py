class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = sorted(arr)
        res = -1
        l=0
        while l<=len(a)-1:
            r = l+1
            
            while r<len(a) and a[r] == a[r-1]:
                #print(r, a[r], l)
                r+=1
                
            if a[r-1]==r-l:
                res=max(res, r-l)
            l=r
        return res
            