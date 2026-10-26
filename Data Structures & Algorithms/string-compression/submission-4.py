class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j =0

        while i<len(chars):
            cur,c = chars[i], 0
            while i<len(chars) and cur==chars[i]:
                i+=1
                c+=1
            chars[j] = cur
            j+=1
            if c>1:
                c = str(c)
                for n in c:
                    chars[j] = n
                    j+=1
        print(chars, j)
        return j