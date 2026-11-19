class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.n = maxNumbers
        self.numbers = [ i for i in range(maxNumbers)]
        self.firstempty = 0

    def get(self) -> int:
        if len(self.numbers) == 0:
            return -1
        
        return self.numbers.pop(0)

    def check(self, number: int) -> bool:
        return number in self.numbers
            

    def release(self, number: int) -> None:
        self.numbers.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
