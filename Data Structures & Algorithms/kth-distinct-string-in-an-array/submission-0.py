class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0)+1
        
        
        for i in arr:
            if counts[i]==1:
                k-=1
                if k==0:
                    return i
        
        return ""