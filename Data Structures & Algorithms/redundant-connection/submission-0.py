class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1]*(n+1)
        
        def find(e1):
            if e1 != parents[e1]:
                parents[e1] = find(parents[e1])
            return parents[e1]

        def union(e1, e2):
            print(e1)
            p1, p2 = find(e1), find(e2)
            if p1==p2:
                return False

            if rank[p1]>rank[p2]:
                parents[p2] = p1
                rank[p2] += rank[p1]
            else:
                parents[p1] = p2
                rank[p1] += rank[p2]


                 
            return True
        
        for e1, e2 in edges:
            
            if not union(e1, e2):
                return [e1, e2]
            