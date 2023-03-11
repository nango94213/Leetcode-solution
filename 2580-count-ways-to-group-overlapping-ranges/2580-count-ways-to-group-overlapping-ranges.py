class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        n = len(ranges)
        stack = []
        
        for n in ranges:
            if stack and n[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], n[1])
            else:
                stack.append(n)
        return 2 ** len(stack) % (10**9 + 7)
        