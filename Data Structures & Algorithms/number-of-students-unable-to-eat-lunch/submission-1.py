class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        m = {1:0, 0:0}
        for i in students:
            m[i] = m.get(i, 0)+1
        
        for s in sandwiches:

            m[s]-=1
        
            if m[s]<0:
                break
        res = 0
        for i in m.values():
            if i>=0:
                res+=i
        return res