class HashTable:
    
    def __init__(self, capacity: int):
        self.v = {}
        self.n = 0
        self.total = capacity

    def insert(self, key: int, value: int) -> None:
        if key not in self.v.keys():
            self.n+=1
        self.v[key] = value
        
        if self.n/self.total>=0.5:
            self.resize()
        

    def get(self, key: int) -> int:
        if key not in self.v.keys():
            return -1
        return self.v[key]

    def remove(self, key: int) -> bool:
        if key not in self.v.keys():
            return False
        
        self.n-=1
        del self.v[key]
        return True

    def getSize(self) -> int:
        return self.n

    def getCapacity(self) -> int:
        return self.total

    def resize(self) -> None:
        self.total = self.total*2

