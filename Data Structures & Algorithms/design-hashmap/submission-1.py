class MyHashMap:

    def __init__(self):
        self.m = {}

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        return self.m[key] 

    def remove(self, key: int) -> None:
        if key in self.m:
            self.m.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)