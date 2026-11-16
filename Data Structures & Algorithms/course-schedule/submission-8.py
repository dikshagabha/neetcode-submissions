class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()
        setn = defaultdict(list)
        for src, dest in prerequisites:
            setn[src].append(dest)

        def dfs(edge):
            if edge in visited:
                return True
            
            if edge in visiting:
                return False
            visiting.add(edge)
            for i in setn[edge]:
                if not dfs(i):
                    return False
            visiting.remove(edge)
            visited.add(edge)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True