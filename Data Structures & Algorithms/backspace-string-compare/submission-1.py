class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_lists(s):
            st = []
            for i in s:
                if i=='#':
                    if len(st):
                        st.pop()
                    continue
                st.append(i)
            return st
        return get_lists(s)==get_lists(t)