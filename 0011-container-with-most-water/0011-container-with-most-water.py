class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            total = (right - left) * min(height[left], height[right])
            res = max(total, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res