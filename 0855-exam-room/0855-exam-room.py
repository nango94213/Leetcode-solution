import bisect
class ExamRoom:

    def __init__(self, n: int):
        self.seats = []
        self.n = n

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        s = 0
        d = self.seats[0]
        
        for a, b in zip(self.seats, self.seats[1:]):
            if (b-a) // 2 > d:
                s = (a+b) // 2
                d = (b-a) // 2
        if self.n - 1 - self.seats[-1] > d:
            s = self.n - 1
        bisect.insort(self.seats, s)
        return s

    def leave(self, p: int) -> None:
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)