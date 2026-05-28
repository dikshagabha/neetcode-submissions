class Solution:
    def stringMatching(self, l: List[str]) -> List[str]:
      
        l.sort(key=len)
     
        res = []
        for i in range(len(l)):
            for j in range(i+1,len(l) ):
                if l[i] in l[j]:
                    res.append(l[i])
                    break
        return res