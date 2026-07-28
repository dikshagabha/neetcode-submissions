class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            cur = s[i]
            if cur!=']':
                st.append(cur)
                continue
            
            curstring = ''
            while st[-1] !='[':
                curstring=st.pop()+curstring
            st.pop()
            multiply = ''
            while st and st[-1].isdigit():
                multiply=st.pop() + multiply
            st.append(curstring*int(multiply))
        return ''.join(st)
        
