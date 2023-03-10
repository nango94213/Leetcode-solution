class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        n = len(ranges)
        stack = [ranges[0]]
        
        for i in range(1, n):
            if ranges[i][0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], ranges[i][1])
            else:
                stack.append(ranges[i])
        return 2 ** len(stack) % (10**9 + 7)
        