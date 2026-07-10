class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word==abbr:
            return True
        
        i=0
        j=0
        while i<len(word) and j<len(abbr):
            if word[i]==abbr[j]:
                while i<len(word) and j<len(abbr) and word[i]==abbr[j]:
                    i+=1
                    j+=1
                continue
            if abbr[j]=='0':
                return False
            c = ''
            while j<len(abbr) and ord(abbr[j])<=57 and ord(abbr[j])>=48:
                c+=abbr[j]
                j+=1
            if len(c)<1:
                return False
            
            c= int(c)
            i+=c
        print(i, j)
        return i==len(word) and j==len(abbr)    