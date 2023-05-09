class FrequencyTracker:

    def __init__(self):
        self.count = Counter()
        self.count2 = Counter()
        

    def add(self, number: int) -> None:
        self.count[number] += 1
        self.count2[self.count[number]] += 1
        self.count2[self.count[number]-1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] > 0:
            self.count[number] -= 1
            self.count2[self.count[number]] += 1
            self.count2[self.count[number]+1] -= 1
        

    def hasFrequency(self, frequency: int) -> bool:
        if self.count2[frequency] > 0:
            return True
        else:
            return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)