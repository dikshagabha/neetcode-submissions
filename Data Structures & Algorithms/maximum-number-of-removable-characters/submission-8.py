class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def issubstring(source, subseq):
            l1, l2= 0, 0
            while l1<len(source) and l2<len(subseq):
                if source[l1] == subseq[l2]:
                    l2+=1
                l1+=1
            return l2==len(subseq)
        removed = set()
        l = 0
        n = r = len(removable)
       
        while r>l:
            temp = list(s)
            mid = l + (r-l)//2
            for i in range(mid+1):
                temp[removable[i]] = ''
            if issubstring(temp, p):
                l = mid+1
            else:
                r=mid 
        return l