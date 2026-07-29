class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        nei = {}
        for i in range(numCourses):
            nei[i] = []
        for src, dest in prerequisites:
            nei[src].append(dest)
        #print(nei)
        path = []
        visited=set()
        res = []
        def detect_cycle(i):
            if i in visited:
                return False
            if i in path:
                return True
            
            visited.add(i)
            for req in nei[i]:
                if detect_cycle(req)==False:
                    return False
            visited.remove(i)
            path.append(i)
            
            return True

        for i in range(numCourses):
            if detect_cycle(i)==False:
                return []
        path += [i for i in range(max(path)+1, numCourses)]
        return path
