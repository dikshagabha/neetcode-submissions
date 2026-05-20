class Solution:
    def decodeString(self, s: str) -> str:
        repeat=[]
        start = "["
        end = "]"
        stack = []
        i=0

        for i in range(len(s)):
            if s[i]==end:
                print(stack)
                cur = ""
                while stack[-1] != start:
                    k = stack.pop()
                    cur = k+cur
                stack.pop()
                digit = ""
                while len(stack) and stack[-1].isdigit():
                    digit = stack.pop()+digit
                
                stack.append(cur*int(digit))
                continue

            
            stack.append(s[i])
        return  "".join(stack)
        # while i<len(s):
        #     print(i)
        #     if s[i]==start:
        #         i+=1
        #         continue
        #     if s[i].isdigit():
        #         cur = ""
        #         while i<len(s) and s[i] != start:
        #             cur +=s[i]
        #             i+=1
        #         repeat.append(int(cur))
        #         continue
        #     cur = ''
        #     while i<len(s) and s[i]!=end and not s[i].isdigit():
        #         cur+=s[i]
        #         i+=1
        #     if len(cur):
        #         strings.append(cur)   
        #         continue
        #     if len(repeat) and s[i]==end:
        #         k = strings.pop()
        #         k = k*repeat.pop()
        #         new_s = ""
        #         if len(strings):
        #             new_s = strings.pop()
        #         new_s = new_s+k
        #         strings.append(new_s)
        #     print(strings, repeat)
        #     i+=1
            
        # return  "".join(strings)
        
        
        
