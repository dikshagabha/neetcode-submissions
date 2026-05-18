class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            m[i]=m.get(i,0)+1
        s=[]
        for i in nums:
            s.append([])
        #print(s)
        for num, c in m.items():
            s[c-1].append(num)
        res=[]
        #print(s)
        j = len(nums)-1
        while j>=0 and k>0:
            if s[j] == []:
                j-=1
                continue
            #print(s[j], k)
            res.extend(s[j][:k])
            k-=len(s[j])
            j-=1
           
        
        return res
            
            

