class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber<=26:
            return chr(64 +columnNumber)
        
        res = ''
        while columnNumber:
            res = chr((columnNumber-1)%26+ord('A'))+res
            columnNumber = (columnNumber-1)//26
            
        return res