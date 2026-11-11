class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        rdmap = collections.defaultdict(list)
        blmap = collections.defaultdict(list)
        for src, dest in redEdges:
            
            rdmap[src].append(dest)
        
        for src, dest in blueEdges:
            
            blmap[src].append(dest)
        
        q = deque()
        q.append((0, 0, None))
        visit = set()
        visit.add((0, None))
        res = [-1 for _ in range(n)]
        while q:
            node, leng, color = q.popleft()
            if res[node] == -1:
                res[node] = leng
            
            if color != 'RED':
                for dest in rdmap[node]:
                    if (dest, 'RED') not in visit:
                        visit.add((dest, 'RED'))
                        q.append((dest, leng+1, 'RED'))
            if color != 'BLUE':
                for dest in blmap[node]:
                    if (dest, 'BLUE') not in visit:
                        visit.add((dest, 'BLUE'))
                        q.append((dest, leng+1, 'BLUE'))
        return res

