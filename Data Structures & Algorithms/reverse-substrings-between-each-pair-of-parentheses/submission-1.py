class Solution:
    def reverseParentheses(self, s: str) -> str:
        q = deque()
        i = 0
        while i<len(s):
            if s[i] == ')':
                t = []
                while q[-1] != '(':
                    c = q.pop()
                    t.append(c)
                q.pop()
                q.extend(t)
                i+=1
                continue

            q.append(s[i])
            i+=1
        return ''.join(q)