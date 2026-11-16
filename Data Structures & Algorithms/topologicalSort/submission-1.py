class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        setn = defaultdict(list)
        for src, dest in edges:
            setn[src].append(dest)
        visited = set()
        res = []
        visiting = set()
        def dfs(edge):
            nonlocal res
            nonlocal visited
            if edge in visited:
                return True
            if edge in visiting:
                return False
            
            visiting.add(edge)
            if len(setn[edge])==0:
                visited.add(edge)
                res.append(edge)
            for i in setn[edge]:
                if not  dfs(i):
                    return False
               
            visiting.remove(edge)
            res.append(edge)
            visited.add(edge)
            return True

                
        for src in range(n):
            dfs(src)

        res.reverse()
        return res
    