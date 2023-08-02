class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total = 0
        for h in hours:
            if h >= target:
                total += 1
        return total
        