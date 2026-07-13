class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruitsmap = {}
        # for i in fruits:
        #     fruitsmap[i] = fruitsmap.get(i, 0)+1
        
        # if len(fruitsmap)<=2:
        #     return len(fruits)
        n = len(fruits)
        l = 0
        visited = {}
        
        res = 0
        for r in range(n):
            visited[fruits[r]] = visited.get(fruits[r],0)+1
            while l<r and len(visited)>=3:
                visited[fruits[l]]-=1
                if visited[fruits[l]] ==0:
                    visited.pop(fruits[l])
                l+=1
            res = max(res, sum(visited.values()))
        return res



