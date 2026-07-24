class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1]*n
        parents = [i for i in range(n)]
       
        
        def get_root(n):
            res = n
            while res!=parents[res]:
                res = parents[res]
            return res
        
        def union(n1, n2):
            p1, p2 = get_root(n1), get_root(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for e1, e2 in edges:
            k = union(e1, e2)
            
            if k==0:
                return False
            res-=k
        return res==1