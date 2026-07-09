class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        nei = {}
        for src, dest in prerequisites:
            if src not in nei:
                nei[src] = []
            nei[src].append(dest)
        
        path = []

        def create_path(i):
            if i in path:
                return False
            if i not in nei or len(nei[i])==0:
                return True

            if i==numCourses-1 and i not in nei.keys():
                return True

            res = False
            path.append(i)
            
            for dests in nei[i]:
                if not create_path(dests):
                    return False
            
            path.pop()
            nei[i] = []
            return True

        for c in range(numCourses):
                if not create_path(c):
                    return False
        return True
        # # print(path)
        return create_path(0)
        

