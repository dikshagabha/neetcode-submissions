class Solution:
    def decodeString(self, inputstring: str) -> str:
        s = []
        res = ""
        i=0
        while i<len(inputstring):
            st = inputstring[i]
            if inputstring[i] != ']':
                s.append(st)
                i+=1
                continue
            cur = []
            while s[-1] != '[':
                c = s.pop()
                cur = [c]+cur
            s.pop()
            multiplier = ''
            while len(s) and 48<=ord(s[-1])<=57:
                c = s.pop()
                multiplier = c + multiplier
                
            s.extend(cur*int(multiplier))
            i+=1
        
           
        return ''.join(s)
