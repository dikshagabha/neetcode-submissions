class PrefixTree:

    def __init__(self):
        self.strings = []

    def insert(self, word: str) -> None:
        self.strings.append(word)
        self.strings.sort()

    def search(self, word: str) -> bool:
        # or we can do a binary search
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
        