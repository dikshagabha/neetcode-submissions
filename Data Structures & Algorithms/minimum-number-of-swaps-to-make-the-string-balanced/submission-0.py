class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for i in s:
            if i=='[':
                st.append(i)
            elif st:
                st.pop()
        return (len(st)+1)//2