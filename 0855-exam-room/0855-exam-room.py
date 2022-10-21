class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.student = []
        

    def seat(self) -> int:
        if not self.student:
            self.student.append(0)
            return 0
        
        d = self.student[0]
        res = 0
        
        for a, b in zip(self.student, self.student[1:]):
            if (b-a) // 2 > d:
                d = (b-a) // 2
                res = (a+b) // 2
        if (self.n-1) - self.student[-1] > d:
            res = self.n - 1
        bisect.insort(self.student, res)
        return res
        

    def leave(self, p: int) -> None:
        self.student.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)