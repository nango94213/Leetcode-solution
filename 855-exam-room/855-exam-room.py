class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.L = []
        

    def seat(self) -> int:
        if not self.L:
            res = 0
        else:
            d, res = self.L[0], 0
            for a, b in zip(self.L, self.L[1:]):
                if (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            if ((self.n - 1) - self.L[-1]) > d:
                res = self.n - 1
        bisect.insort(self.L, res)
        return res
        

    def leave(self, p: int) -> None:
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)