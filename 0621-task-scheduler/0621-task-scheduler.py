class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = sorted(Counter(tasks).values())
        slot = (count.pop() - 1)
        total = slot * n
        
        while total and count:
            current = count.pop()
            total -= min(slot, current)
        
        total = max(0, total)
        
        return len(tasks) + total
        