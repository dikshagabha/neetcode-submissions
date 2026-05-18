class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts  = {}
        for i in nums:
            counts[i] = counts.get(i, 0)+1
        
        n = len(nums)
        elements = [[] for i in range(n)]
        for key, count in counts.items():
            elements[count-1].append(key)
        print(elements)
        res = []
        i=n-1
        while i>=0:
            if len(elements[i])==0:
                i-=1
                continue
            if k<=0:
                break
            res.extend(elements[i])
            k-=len(elements[i])
            i-=1
        
        return res