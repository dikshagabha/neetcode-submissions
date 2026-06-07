class PrefixTree:

    def __init__(self):
        self.strings = []

    def insert(self, word: str) -> None:
        self.strings.append(word)
        self.strings.sort()

    def search(self, word: str) -> bool:
        # or we can do a binary search
        # l = 0
        # r= len(self.strings)-1
        
        # while l<r:
        #     mid = l+((r-l)//2)
        #     #print(word, self.strings, mid, l, r)
        #     if word == self.strings[mid]:
                
        #         return True
        #     if word[0]>self.strings[mid][0]:
        #         l = mid+1
        #     else:
        #         r = mid-1
        #     return False


        if word in self.strings:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        # do a binary search on start
        n = len(prefix)
        for i in self.strings:
            if i[:n] == prefix:
                return True
        return False
        