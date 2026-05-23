class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = [0]*(len(nums)+1)
        h = {}
        for i in nums:
            h[i] = h.get(i, 0)+1
        #print(h)
        for i, count in h.items():
            if m[count] == 0:
                m[count]=[]
            m[count].append(i)
        
        #print(m)
        res = []
        for j in range(len(m)-1, -1, -1):
            if k==0:
                return res
           
            while k>0 and m[j]:
                cur = m[j].pop()
                res.append(cur)
                k-=1
        return res